import glob
import nltk
from nltk.tokenize import word_tokenize
from rich.progress import Progress
from rich.console import Console
import matplotlib.pyplot as plt

progress = Progress()
console = Console()

# Uncomment the following line to download the required models
# nltk.download('punkt')  # tokenizer models

token_list = []
word_counts = {}
total_files = len(glob.glob("crititcalrole/*.txt"))
# Spells_to_Count = ['water breathing', 'hex', 'rage']  # for testing
Spells_to_Count = []

with open("SpellsOuput.txt", "r") as file:
    Spells_to_Count = file.read().splitlines()

Spell_counts = {}
for Spells in Spells_to_Count:
    Spell_counts[Spells] = 0


with progress:
    task = progress.add_task("[green]Processing files...", total=total_files)

    # Iterate over all text files in the folder
    for file_path in glob.glob("crititcalrole/*.txt"):
        with open(file_path, 'r', encoding='utf-8') as file:  # Open
            text = file.read()  # Read
            tokens = word_tokenize(text)  # Tokenize
            token_list.extend(tokens)  # Add to list

            # Count the occurrences of each word
            for word in tokens:
                word_counts[word] = word_counts.get(word, 0) + 1

            # Count the occurrences of each Spells
            for Spells in Spells_to_Count:
                Spell_counts[Spells] += text.count(Spells)

        # Advance the progress tracker
        progress.advance(task)

# Print the occurrences of each word
for word, count in word_counts.items():
    print(word + ' count: ' + str(count))

# Print the occurrences of each Spells
print("\nOccurrences of Spells:")
for Spells, count in Spell_counts.items():
    print(Spells + ' count: ' + str(count))

# sort Spells by count
sorted_Spells = sorted(Spell_counts.items(), key=lambda x: x[1], reverse=True)
# print top 10 Spells
print("\nTop 10 Spells:")
for Spells, count in sorted_Spells[:10]:
    print(Spells + ' count: ' + str(count))

#graph it using matplotlib
x_values = [x[0] for x in sorted_Spells[:30]]
y_values = [y[1] for y in sorted_Spells[:30]]
plt.bar(x_values, y_values)
plt.xlabel('Spells')
plt.ylabel('Count')
plt.title('Top 30 Spells')
plt.xticks(rotation=65)
plt.tight_layout()
plt.show()




