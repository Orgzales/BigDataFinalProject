import glob
import nltk
from nltk.tokenize import word_tokenize
from rich.progress import Progress
from rich.console import Console
import pandas as pd

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
files_with_level_up = []  # To track which files contain "level up"
total_files_with_level_up = 0 #for testing

token_list = []
word_counts = {}

with progress:
    task = progress.add_task("[green]Processing files...", total=total_files)
    for file_path in glob.glob("crititcalrole/(2x01)_CuriousBeginnings.txt"):

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
        progress.advance(task)

for file_path, counts in spell_counts_per_file.items():
    print("File: " + str(file_path))
    for spell, count in counts.items():
        print(spell + ": " + str(count))

# Count the total occurrences of each spell and print the total with the spell name
Spell_total_counts = {}
for file_path, counts in spell_counts_per_file.items():
    for spell, count in counts.items():
        if spell in Spell_total_counts:
            Spell_total_counts[spell] += count
        else:
            Spell_total_counts[spell] = count

# Display the total count of level up
print("Total 'level up' count:", total_files_with_level_up)
print("Files with 'level up':", files_with_level_up)


print("!!!!!!!!!!!!!!!!!!!!!!")
# print the total count of each spell only if is greater than 0
for spell, count in Spell_total_counts.items():
    if count > 0:
        print(spell + ": " + str(count))
        #print out the calsses value for each spell
        print(spell_classes_values[spell_names_values.tolist().index(spell)])

df_characters = pd.read_csv("Charaters.csv")

character_names = df_characters['Name'].unique()  # Unique character names
character_classes = df_characters['Class'].unique()  # Unique character classes
character_spells = df_characters['Spells'].unique()  # Unique character spells

character_success_rate = {} #store the success rate of each character

#Check if each charater has the spell or not | or class can have the spell
for character in character_names:
    sucesss_rate = 0.0 #testing
    character_class = character_classes[character_names.tolist().index(character)]
    class_text = character_class.split(" ")[0] #to get rid of the extra text in the class column
    # level_text = character_class.split(" ")[1] #to get the level to add to the susscess rate
    # sucesss_rate = sucesss_rate + int(level_text) #add the level to the success rate

    for spell in spell_counts: #go throgh each spell (change to each session later)
        if Spell_total_counts[spell] > 0: # if it has been used in the session
            spell_occurance = Spell_total_counts[spell] # total num of times the spell has been used
            spell_class = spell_classes_values[spell_names_values.tolist().index(spell)] # the classes that could use the spell
            # print ("Spell: " + spell)
            if spell in character_spells[character_names.tolist().index(character)]:
                print(character + " has " + spell + " spell")
                sucesss_rate = (spell_occurance * 2) + sucesss_rate
            elif class_text in spell_class:
                print(character_classes[character_names.tolist().index(character)])
                print(spell_class)
                print(character + " can obtain " + spell + " spell")
                sucesss_rate = spell_occurance + sucesss_rate
                # print("Spell class: " + spell_class)
                # print("Character class: " + character_classes[character_names.tolist().index(character)])
    print("success rate for " + character + " is: " + str(sucesss_rate) + "%")
    character_success_rate[character] = sucesss_rate

#print all the characters and their success rate sorted from best to worst
print("!!!!!!!!!!!!!!!!!!!!!!")
print("Characters and their success rate sorted from best to worst in session 1:")
for character, rate in sorted(character_success_rate.items(), key=lambda item: item[1], reverse=True):
    print(character + ": " + str(rate) + "%")


print("!!!!!!!!!!!!!!!!!!!!!!")
#getting the level and class of each subclass
for character in character_names:
    character_class = character_classes[character_names.tolist().index(character)]
    class_text = character_class.split("|")  # to get rid of the extra text in the class column
    print (class_text)
    # level_text = character_class.split(" ")[1] #to get the level to add to the susscess rate
    # sucesss_rate = sucesss_rate + int(level_text) #add the level to the success rate
    for string in class_text:
        name_class = string.split(" ")[0]
        level_class = string.split(" ")[1]
        print(name_class)
        print(level_class)
    print("!!!!!!!!!!!!!!!!!!!!!!")


# print out the top 10 most common words
print("!!!!!!!!!!!!!!!!!!!!!!")
print("Top 10 most common words:")
for word, count in sorted(word_counts.items(), key=lambda item: item[1], reverse=True)[:10]:
    print(word + ": " + str(count))

# for each charater, find how often their skills would be used in the sesssions
print("!!!!!!!!!!!!!!!!!!!!!!")
for character in character_names:
    character_skills = df_characters['Skills'][character_names.tolist().index(character)]
    print(character + " skills: " + character_skills)
    skills_split = character_skills.split("|")
    for skill in skills_split:
        print(skill)
        for word, count in word_counts.items():
            if skill.lower() in word:
                print(word + ": " + str(count))



