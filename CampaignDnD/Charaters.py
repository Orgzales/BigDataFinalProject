import pandas as pd
import csv

df = pd.read_csv("DndData/Charaters.csv")

#pulling data that is useful only for the characters
column_names = df.columns.tolist()
#[' ip', 'finger', 'hash', 'name', 'race', 'background', 'date', 'class', 'justClass', 'subclass',
# 'level', 'feats', 'HP', 'AC', 'Str', 'Dex', 'Con', 'Int', 'Wis', 'Cha', 'alignment', 'skills', 'weapons',
# 'spells', 'castingStat', 'choices', 'country', 'countryCode', 'processedAlignment', 'good', 'lawful',
# 'processedRace', 'processedSpells', 'processedWeapons', 'alias']
print("Column Names:", column_names)


Name_Column = df.columns[df.columns.get_loc('name')] #names column
Class_Column = df.columns[df.columns.get_loc('class')] #class column
processedSpells_Column = df.columns[df.columns.get_loc('processedSpells')] #spells column
skills_Column = df.columns[df.columns.get_loc('skills')] #skills column

count = 0
output_file_path = "Charaters.csv"

with open(output_file_path, "w", newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Name", "Class", "Spells", "Skills"])  # Header

    name_values = df[Name_Column].unique()
    class_values = df[Class_Column].unique()
    spells_values = df[processedSpells_Column].unique()
    skills_values = df[skills_Column].unique()

    for name in name_values:
        if count >= 10:  # testing
            break
        print(name)
        csv_writer.writerow([name, class_values[count], spells_values[count], skills_values[count]])
        count += 1

    # for Class in class_values:
    #     if count >= 10:
    #         break
    #     count += 1
    #     print(Class)
    #     csv_writer.writerow([Class])
    # for spells in spells_values:
    #     if count >= 10:
    #         break
    #     count += 1
    #     print(spells)
    #     csv_writer.writerow([spells])
    # for skills in skills_values:
    #     if count >= 10:
    #         break
    #     count += 1
    #     print(skills)
    #     csv_writer.writerow([skills])

#spells
# count = 0
# output_file_path = "Charaters.txt"
# with open(output_file_path, "w") as file:
#     # Print unique values and write them to the file simultaneously
#     print("Unique Values in Column:", Name_Column)
#     name_values = df[Name_Column].unique()
#     for name in name_values:
#         if count >= 10:  # testing
#             break
#         count += 1
#         print(name)
#         file.write(str(name) + "\n")
#
# df = pd.read_csv("DndData/Charaters_unquie.csv")
# Name_Column = df.columns[7] #names column



# #class abilites
# output_file_path = "AbilitiesOutput.txt"
# with open(output_file_path, "w") as file:
#     for ability in abilities:
#         print(ability)
#         file.write(str(ability) + "\n")
