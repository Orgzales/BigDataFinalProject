import pandas as pd
import csv

abilities = ["Rage", "Bardic Inspiration", "Channel Divinity", "Wild Shape", "Action Surge", "Martial Arts", "Divine Smite",
             "Hunter's Mark", "Sneak Attack", "Metamagic", "Pact Magic", "Arcane Recovery"]
abilities_classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]

df = pd.read_csv("DndData/dnd-spells.csv")
column_names = df.columns.tolist()
# ['name', 'classes', 'level', 'school', 'cast_time', 'range', 'duration',
# 'verbal', 'somatic', 'material', 'material_cost', 'description']

name_values = df['name']
class_values = df['classes']

print(name_values)

count = 0
output_file_path = "SpellsOutput.csv"

with open(output_file_path, "w", newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Name", "Classes"])  # Header
    print(class_values)
    for name in name_values:
        print(name)
        print(class_values)
        csv_writer.writerow([name, class_values[count]])
        count += 1
    count = 0
    for ability in abilities:
        print(ability)
        csv_writer.writerow([ability, abilities_classes[count]])
        count += 1



# # spells
# output_file_path = "SpellsOuput.txt"
# with open(output_file_path, "w") as file:
#     # Print unique values and write them to the file simultaneously
#     for name in name_values:
#         print(name)
#         file.write(str(name) + "\n")



#class abilites
# output_file_path = "AbilitiesOutput.txt"
# with open(output_file_path, "w") as file:
#     for ability in abilities:
#         print(ability)
#         file.write(str(ability) + "\n")
