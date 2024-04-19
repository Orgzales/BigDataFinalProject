import glob
import nltk
from nltk.tokenize import word_tokenize
from rich.progress import Progress
from rich.console import Console

progress = Progress()
console = Console()

# Uncomment the following line to download the required models
# nltk.download('punkt')  # tokenizer models

token_list = []
word_counts = {}
total_files = len(glob.glob("crititcalrole/*.txt"))
# phrases_to_count = ['water breathing', 'hex', 'rage']  # for testing
phrases_to_count = []

with open("SpellsOuput.txt", "r") as file:
    phrases_to_count = file.read().splitlines()

phrase_counts = {}
for phrase in phrases_to_count:
    phrase_counts[phrase] = 0


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

            # Count the occurrences of each phrase
            for phrase in phrases_to_count:
                phrase_counts[phrase] += text.count(phrase)

        # Advance the progress tracker
        progress.advance(task)

# Print the occurrences of each word
for word, count in word_counts.items():
    print('word: ' + word + ' count: ' + str(count))

# Print the occurrences of each phrase
print("\nOccurrences of phrases:")
for phrase, count in phrase_counts.items():
    print('Phrase: ' + phrase + ' count: ' + str(count))
