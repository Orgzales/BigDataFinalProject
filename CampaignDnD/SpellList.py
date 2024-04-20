import pandas as pd
import csv

abilities = ["Rage", "Bardic Inspiration", "Channel Divinity", "Wild Shape", "Action Surge", "Martial Arts", "Divine Smite",
             "Hunter's Mark", "Sneak Attack", "Metamagic", "Pact Magic", "Arcane Recovery"]

df = pd.read_csv("DndData/dnd-spells.csv")
column_names = df.columns.tolist()
# ['name', 'classes', 'level', 'school', 'cast_time', 'range', 'duration',
# 'verbal', 'somatic', 'material', 'material_cost', 'description']

Name_Column = df.columns[df.columns.get_loc('name')] #names column
Class_Column = df.columns[df.columns.get_loc('classes')] #class column

count = 0
output_file_path = "SpellsOutput.csv"

with open(output_file_path, "w", newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Name", "Classes"])  # Header

    name_values = df[Name_Column].unique()
    class_values = df[Class_Column].unique()

    for name in name_values:
        print(name)
        csv_writer.writerow([name, class_values[count]])
        count += 1

#spells
# output_file_path = "SpellsOuput.txt"
# with open(output_file_path, "w") as file:
#     # Print unique values and write them to the file simultaneously
#     print("Unique Values in Column:", Name_Column)
#     name_values = df[Name_Column].unique()
#     for name in name_values:
#         print(name)
#         file.write(str(name) + "\n")

#class abilites
# output_file_path = "AbilitiesOutput.txt"
# with open(output_file_path, "w") as file:
#     for ability in abilities:
#         print(ability)
#         file.write(str(ability) + "\n")
