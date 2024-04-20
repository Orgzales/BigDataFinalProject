import pandas as pd
import csv

abilities = ["Rage", "Bardic Inspiration", "Channel Divinity", "Wild Shape", "Action Surge", "Martial Arts", "Divine Smite",
             "Hunter's Mark", "Sneak Attack", "Metamagic", "Pact Magic", "Arcane Recovery"]

df = pd.read_csv("DndData/dnd-spells.csv")
column_names = df.columns.tolist()
# ['name', 'classes', 'level', 'school', 'cast_time', 'range', 'duration',
# 'verbal', 'somatic', 'material', 'material_cost', 'description']

name_values = df['name'].unique()
class_values = df['classes'].unique()

count = 0
output_file_path = "SpellsOutput.csv"

with open(output_file_path, "w", newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Name", "Classes"])  # Header

    for name in name_values:
        print(name)
        csv_writer.writerow([name, class_values[count]])
        count += 1

# spells
output_file_path = "SpellsOuput.txt"
with open(output_file_path, "w") as file:
    # Print unique values and write them to the file simultaneously
    for name in name_values:
        print(name)
        file.write(str(name) + "\n")

#class abilites
# output_file_path = "AbilitiesOutput.txt"
# with open(output_file_path, "w") as file:
#     for ability in abilities:
#         print(ability)
#         file.write(str(ability) + "\n")
