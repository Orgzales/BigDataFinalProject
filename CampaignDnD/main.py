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

total_files = len(glob.glob("crititcalrole/*.txt"))

df = pd.read_csv("SpellsOutput.csv")
spell_names_column = df.columns[df.columns.get_loc('Name')] #names column
spell_names_values = df[spell_names_column].unique()

spell_counts_per_file = {} #  store the count of each spell in each file
files_with_level_up = []  # To track which files contain "level up"
total_files_with_level_up = 0 #for testing


with progress:
    task = progress.add_task("[green]Processing files...", total=total_files)
    for file_path in glob.glob("crititcalrole/*.txt"):

        spell_counts = {}
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read().lower()
            # tokens = word_tokenize(text)

            # Count the occurrences of each spell
            for spell in spell_names_values:
                spell = spell.lower()
                spell_counts[spell] = text.count(spell)

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

print("!!!!!!!!!!!!!!!!!!!!!!")
#print the total count of each spell only if is greater than 0
for spell, count in Spell_total_counts.items():
    if count > 0:
        print(spell + ": " + str(count))

# Display the total count
# print("Total 'level up' count:", total_files_with_level_up)
# print("Files with 'level up':", files_with_level_up)




#
# #graph it using matplotlib
# x_values = [x[0] for x in sorted_Spells[:30]]
# y_values = [y[1] for y in sorted_Spells[:30]]
# plt.bar(x_values, y_values)
# plt.xlabel('Spells')
# plt.ylabel('Count')
# plt.title('Top 30 Spells')
# plt.xticks(rotation=65)
# plt.tight_layout()
# plt.show()




