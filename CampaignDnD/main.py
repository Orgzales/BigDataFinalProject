import glob
import nltk
from nltk.tokenize import word_tokenize
from rich.progress import Progress
from rich.console import Console
import pandas as pd
import re

progress = Progress()
console = Console()

# Uncomment the following line to download the required models
# nltk.download('punkt')  # tokenizer models

total_files = len(glob.glob("crititcalrole/(2x01)_CuriousBeginnings.txt"))
# total_files = len(glob.glob("crititcalrole/*.txt"))

df_spells = pd.read_csv("SpellsOutput.csv")
spell_names_values = df_spells['Name']#spell names column
spell_classes_values = df_spells['Classes'] #spell classes column

spell_counts_per_file = {} #  store the count of each spell in each file
word_counts_per_file = {} # store the count of each word in each file
files_with_level_up = []  # To track which files contain "level up"
total_files_with_level_up = 0 #for testing

token_list = [] #store all the tokens in all files


with progress:
    task = progress.add_task("[green]Processing files...", total=total_files)
    for file_path in glob.glob("crititcalrole/testing/*.txt"):

        word_counts = {}
        spell_counts = {}
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read().lower()
            tokens = word_tokenize(text)
            token_list.extend(tokens)

            #count each occurrence of each word
            for word in tokens:
                word_counts[word] = word_counts.get(word, 0) + 1

            # Count the occurrences of each spell
            for spell in spell_names_values:
                spell_counts[spell] = text.count(spell.lower())

            if "level up" in text:
                total_files_with_level_up += 1
                files_with_level_up.append(file_path)

        spell_counts_per_file[file_path] = spell_counts
        word_counts_per_file[file_path] = word_counts
        # print(spell_counts_per_file[file_path])
        progress.advance(task)

for file_path, counts in spell_counts_per_file.items():
    print("File: " + str(file_path))
    for spell, count in counts.items():
        if count > 0:
            print(spell + ": " + str(count))

# Count the total occurrences of each spell and print the total with the spell name
Spell_total_counts = {}
for file_path, counts in spell_counts_per_file.items():
    for spell, count in counts.items():
        if spell in Spell_total_counts:
            Spell_total_counts[spell] += count
        else:
            Spell_total_counts[spell] = count
    print("File: " + str(file_path))
    print("Total spell counts: " + str(Spell_total_counts))

# Display the total count of level up
print("Total 'level up' count:", total_files_with_level_up)
print("Files with 'level up':", files_with_level_up)

df_characters = pd.read_csv("Charaters.csv")

character_names = df_characters['Name']  # Unique character names
character_classes = df_characters['Class']  # Unique character classes
character_spells = df_characters['Spells']  # Unique character spells

#dictionary that contains the charater success rate in each file
session_success_rate = {}

#for each file check how many spells that the charater knwon in that file
for file_path, spells_in_session in spell_counts_per_file.items():
    character_success_rate = {}  # store the success rate of each character in the session
    print("Session: " + str(file_path))


    #Check if each charater has the spell or not | or class can have the spell
    for character in character_names:
        # print("!!!!!!!!!!!!!!!!!!!!!!")
        sucesss_rate = 0.0 #testing

        character_class = character_classes[character_names.tolist().index(character)]
        class_text = character_class.split("|")  # to get rid of the extra text in the class column
        print(character + " class: " + character_class)

        for class_name in class_text:
            name_class = class_name.split(" ")[0]
            level_class = class_name.split(" ")[1]

            sucesss_rate = sucesss_rate + int(level_class) #add the level to the success rate
            # print("Level from " + name_class + ": +" + level_class + "%")

            spells_known = []
            spells_leaning = []
            spell_known_rate = 0.0
            spell_learn_rate = 0.0
            for spell in spells_in_session: #go throgh each spell (change to each session later)
                if spells_in_session[spell] > 0: # if it has been used in the session
                    spell_occurance = spells_in_session[spell] # total num of times the spell has been used
                    spell_class = spell_classes_values[spell_names_values.tolist().index(spell)] # the classes that could use the spell
                    if spell in character_spells[character_names.tolist().index(character)]:
                        spell_known_rate = spell_occurance
                        spells_known.append(spell)
                        # print(spell + "(#=" + str(spell_occurance) + ") is known by " + character + " (+ " + str(spell_known_rate) + "%)")
                    elif name_class in spell_class:
                        spell_learn_rate = (spell_occurance/2)
                        spells_leaning.append(spell)
                        # print(spell + "(#=" + str(spell_occurance) + ") is learned by " + character + " (+ " + str(spell_learn_rate) + "%)")

            # print("Spells known (+ " + str(spell_known_rate) + "%) : " + str(spells_known))
            # print("Spells leaning (+ " + str(spell_learn_rate) + "%) : " + str(spells_leaning))
            sucesss_rate = sucesss_rate + spell_known_rate + spell_learn_rate

        character_skills = df_characters['Skills'][character_names.tolist().index(character)]

        skills_split = character_skills.split("|")
        skills_known = []
        skill_rate = 0.0
        for skill in skills_split:
            for word, count in word_counts_per_file[file_path].items():
                if skill.lower() in word:
                    skills_known.append(skill)
                    skill_rate = skill_rate + count
                    # print(skill + " is known by " + character + " (+ " + str(count) + "%)")

        print("Skills known (+ " + str(skill_rate) + "%) : " + str(skills_known))
        sucesss_rate = sucesss_rate + skill_rate

        # print("##################################")
        # print("success rate for " + character + " is: " + str(sucesss_rate) + "%")
        character_success_rate[character] = sucesss_rate
        # print(character_success_rate)

        #add all the success rate of each character in the session to the session success rate dictionary
    session_success_rate[file_path] = character_success_rate
    print(session_success_rate)

print("!!!!!!!!!!!!!!!!!!!!!!")
#print each session collection success rates from all charaters in the session
for file_path in spell_counts_per_file:
    print("Session: " + str(file_path))
    charater_success_rates = session_success_rate[file_path]
    print(charater_success_rates)

#
# # print out the top 10 most common words
# print("!!!!!!!!!!!!!!!!!!!!!!")
# print("Top 10 most common words:")
# for word, count in sorted(word_counts.items(), key=lambda item: item[1], reverse=True)[:10]:
#     print(word + ": " + str(count))


# df_monsters = pd.read_csv("DndData/Dd5e_monsters.csv")
# monster_names = df_monsters['Name'] # monster names
# monster_count = {} #store the count of each monster in the session
#
#
# for file_path in glob.glob("crititcalrole/(2x97)_TheFancyandtheFooled.txt"):
#     monster_counts = {}
#     with open(file_path, 'r', encoding='utf-8') as file:
#         text = file.read().lower()
#         #tokenize the text
#         tokens = word_tokenize(text)
#         for monster in monster_names:
#             #if monster contains " " in its name skip it
#             if " " in monster:
#                 monster_counts[monster] = text.count(monster.lower())
#             else:
#                 monster_counts[monster] = tokens.count(monster.lower())
#     monster_count[file_path] = monster_counts
#
# #print each count of monsters
# for file_path, counts in monster_count.items():
#     print("File: " + str(file_path))
#     print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
#     for monster, count in counts.items():
#         if count > 0:
#             print(monster + ": " + str(count))
#             print("Monster CR: " + str(df_monsters['Challenge rating  (XP)'][monster_names.tolist().index(monster)]))
#
#
#


