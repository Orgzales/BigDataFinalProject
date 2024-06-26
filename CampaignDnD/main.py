import glob
import nltk
from nltk.tokenize import word_tokenize
from rich.progress import Progress
from rich.console import Console
import pandas as pd
import re
import matplotlib.pyplot as plt
import numpy as np
import csv

progress = Progress()
console = Console()

# Uncomment the following line to download the required models
# nltk.download('punkt')  # tokenizer models

# total_files = len(glob.glob("crititcalrole/(2x01)_CuriousBeginnings.txt"))
# total_files = len(glob.glob("crititcalrole/testing/*.txt"))
total_files = len(glob.glob("crititcalrole/*.txt"))

#spells
df_spells = pd.read_csv("SpellsOutput.csv")
spell_names_values = df_spells['Name']#spell names column
spell_classes_values = df_spells['Classes'] #spell classes column
spell_level_values = df_spells['Level'] #spell level column

#monsters
df_monsters = pd.read_csv("DndData/Dd5e_monsters.csv")
monster_names = df_monsters['Name'] # monster names
monster_count = {} #store the count of each monster in the session

spell_counts_per_file = {} #  store the count of each spell in each file
word_counts_per_file = {} # store the count of each word in each file
monster_counts_per_file = {} # store the count of each monster in each file
files_with_level_up = []  # To track which files contain "level up"
total_files_with_level_up = 0 #for testing

token_list = [] #store all the tokens in all files

count = 0
with progress:
    task = progress.add_task("[green]Processing files...", total=total_files)
    for file_path in glob.glob("crititcalrole/*.txt"):
        count += 1
        word_counts = {}
        spell_counts = {}
        monster_counts = {}

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

            for monster in monster_names:
                if " " in monster:
                    monster_counts[monster] = text.count(monster.lower())
                else:
                    monster_counts[monster] = tokens.count(monster.lower()) #to prevent counting the word EX: "ape" in "paper"

            if "level up" in text:
                total_files_with_level_up += 1
                files_with_level_up.append(file_path)

        spell_counts_per_file[file_path] = spell_counts
        word_counts_per_file[file_path] = word_counts
        monster_counts_per_file[file_path] = monster_counts

        progress.advance(task)
        # if count >= 10:
        #     break

# Count the total occurrences of each spell and print the total with the spell name
Spell_total_counts = {}
for file_path, counts in spell_counts_per_file.items():
    for spell, count in counts.items():
        if spell in Spell_total_counts:
            Spell_total_counts[spell] += count
        else:
            Spell_total_counts[spell] = count
    # print("File: " + str(file_path))
    # print("Total spell counts: " + str(Spell_total_counts))

print("!!!!!!!!!!!!!!!!!!!!!!")
# Count the total occurrences of each monster and print the total with the monster name
Monster_total_counts = {}
for file_path, counts in monster_counts_per_file.items():
    for monster, count in counts.items():
        if monster in Monster_total_counts:
            Monster_total_counts[monster] += count
        else:
            Monster_total_counts[monster] = count
    # print("File: " + str(file_path))
    # print("Total monster counts: " + str(Monster_total_counts))

# Display the total count of level up
# print("Total 'level up' count:", total_files_with_level_up)
print("Files with 'level up':", files_with_level_up)

Monster_negitive_rate_perfile = {}

# for each file grab the "Challenge rating  (XP)" of each monster in the file
for file_path, counts in monster_counts_per_file.items():
    print("File: " + str(file_path))
    total_sum = 0.0
    for monster, count in counts.items():
        if count > 0:
            monster_index = monster_names.tolist().index(monster)
            # print(monster + ": " + str(df_monsters['Challenge rating  (XP)'][monster_index]))
            challenge_rating = df_monsters['Challenge rating  (XP)'][monster_index].split(" ")[0]
            if "/" in challenge_rating:
                numerator = challenge_rating.split("/")[0]
                denominator = challenge_rating.split("/")[1]
                challenge_rating = float(numerator)/float(denominator)
            total_sum += float(challenge_rating)
    # print("Total challenge rating: " + str(total_sum/10))
    Monster_negitive_rate_perfile[file_path] = total_sum/10


df_characters = pd.read_csv("Charaters.csv")

character_names = df_characters['Name']  # Unique character names
character_classes = df_characters['Class']  # Unique character classes
character_spells = df_characters['Spells']  # Unique character spells

#dictionary that contains the charater success rate in each file
session_success_rate = {}
permanent_success_level = 0.0

character_index = {name: i for i, name in enumerate(character_names)} #tuplues to make it more optimize for indexing

# DO Splitting First to avoid repeats
character_classes_clean = {}
for character in character_names:
    class_text = character_classes[character_index[character]].split("|")
    name_classes_clean = []
    for class_name in class_text:
        name_of_class, level_class = class_name.split(" ")[:2] #EX Sorcerer 13
        name_classes_clean.append( (name_of_class, int(level_class) ))
    character_classes_clean[character] = name_classes_clean #EX [('Sorcerer', 13), ('Fighter', 5)]

# DO Splitting skills to avoid repeated splitting
character_skills_clean = {}
for character in character_names:
    character_skills_clean[character] = df_characters['Skills'][character_index[character]].split("|") #EX ['Acrobatics', "stealth..."]
    # print(character_skills_clean[character])

##for each file check how many spells that the charater knwon in that file
with progress:
    total_characters = len(character_names) #for progress bar
    for file_path, spells_in_session in spell_counts_per_file.items():

        task = progress.add_task("[red]Processing characters for " + file_path + "...", total=total_characters)
        # print("Session: " + str(file_path))

        character_success_rate = {}  # This is where the success rate of each character in the session
        if file_path in files_with_level_up:
            permanent_success_level += 1 #if the file has "level up" add 1% to the success rate

        for character in character_names:
            # print("Character: " + character)
            success_rate = permanent_success_level
            name_classes_clean = character_classes_clean[character] #EX [('Sorcerer', 13), ('Fighter', 5)]
            success_rate += sum(level_class for assoisiated_class, level_class in name_classes_clean)*2.5 #Add for each class level
            # print("Level from " + character + ": +" + str(sum(level_class for assoisiated_class, level_class in name_classes_clean) * 2.5) + "%")

            spell_known_rate = 0.0
            spell_learn_rate = 0.0

            for spell, occurrence in spells_in_session.items():
                if occurrence > 0:
                    spell_class = spell_classes_values[spell_names_values.tolist().index(spell)]
                    # print(spell_class)
                    if spell in character_spells[character_index[character]]:
                        spell_known_rate += occurrence / 10
                        # print(spell + "(#=" + str(occurrence) + ") is known by " + character + " (+ " + str(spell_known_rate) + "%)")
                    else:
                        if any(name_class in spell_class for name_class, class_text in name_classes_clean):
                            if any(level_class >= spell_level_values[spell_names_values.tolist().index(spell)] for name_class, level_class in name_classes_clean):
                                spell_learn_rate += occurrence / 10
                                # print(spell + "(#=" + str(occurrence) + ") is learned by " + character + " (+ " + str(spell_learn_rate) + "%)")
                            # print(spell + "(#=" + str(occurrence) + ") is learned by " + character + " (+ " + str(spell_learn_rate) + "%)")

            success_rate += spell_known_rate + spell_learn_rate

            skills_known = [] #Where the skills that the character knows
            skill_rate = 0.0
            skills_split = character_skills_clean[character] #EX ['Acrobatics', "stealth..."]
            word_counts_per_file_lower = {word.lower(): count for word, count in word_counts_per_file[file_path].items()} #Converting each word to lower, getting the count for each word + count for each word in file
            # print(word_counts_per_file_lower)

            for skill in skills_split:
                # print(skill)
                skill_lower = skill.lower()
                if any(skill_lower in word for word in word_counts_per_file_lower): #for each skill in word, check if the skill is in the file
                    skill_rate += 2  # +2% for each skill
                    # print(skill + " is known by " + character + " (+ " + str(skill_rate) + "%)")
                    skill_rate += sum( (count/10) for word, count in word_counts_per_file_lower.items() if skill_lower in word) # +0.1 for each occurance of the skill
                    # print(skill + " is known by " + character + " (+ " + str(skill_rate) + "%)")
                    # print(skill + ": " + str(sum( (count/10) for word, count in word_counts_per_file_lower.items() if skill_lower in word)))

            success_rate += skill_rate
            character_success_rate[character] = success_rate - (Monster_negitive_rate_perfile[file_path]) #subtract the monster challenge rating from the success
            progress.advance(task)

            # print(character_success_rate)
            # print("##################################")
        session_success_rate[file_path] = character_success_rate
        # print(session_success_rate)

print("!!!!!!!!!!!!!!!!!!!!!!")

# save each session data dictionaries (charater success rate, spells, and monsters) to a csv file
output_file_path = "SessionData.csv"
with open(output_file_path, "w", newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Session", "Character", "Character_Class","Success Rate (%)"])  # Header
    for file_path in spell_counts_per_file:
        for character, success_rate in session_success_rate[file_path].items():
            csv_writer.writerow([file_path, character, character_classes[character_names.tolist().index(character)], success_rate])
print("Session data saved to", output_file_path)

# #save each session spells, monsters, words count, and level up (which is T or F based if it has Level_up in it's text) to a csv file
# output_file_path = "SessionDataCounts.csv"
# with open(output_file_path, "w", newline='', encoding='utf-8') as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(["Session", "Spells", "Monsters", "Words", "Level_up"])  # Header
#     for file_path in spell_counts_per_file:
#         csv_writer.writerow([file_path, spell_counts_per_file[file_path], monster_counts_per_file[file_path], word_counts_per_file[file_path], "T" if file_path in files_with_level_up else "F"])



# output_file_path = "SessionDataCounts.csv"
# with open(output_file_path, "w", newline='', encoding='utf-8') as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(["Session", "Spells", "Monsters", "Words"])  # Header
#     for file_path in spell_counts_per_file:
#         csv_writer.writerow([file_path, spell_counts_per_file[file_path], monster_counts_per_file[file_path], word_counts_per_file[file_path]])
# print("Session data counts saved to", output_file_path)

