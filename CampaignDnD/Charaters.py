import pandas as pd

df = pd.read_csv("DndData/Charaters.csv")

#pulling data that is useful only for the characters
column_names = df.columns.tolist()
#[' ip', 'finger', 'hash', 'name', 'race', 'background', 'date', 'class', 'justClass', 'subclass',
# 'level', 'feats', 'HP', 'AC', 'Str', 'Dex', 'Con', 'Int', 'Wis', 'Cha', 'alignment', 'skills', 'weapons',
# 'spells', 'castingStat', 'choices', 'country', 'countryCode', 'processedAlignment', 'good', 'lawful',
# 'processedRace', 'processedSpells', 'processedWeapons', 'alias']
print("Column Names:", column_names)


Name_Column = df.columns[df.columns.get_loc('processedSpells')] #names column

# print("first Row:", first_ROW)
print("Column: " + Name_Column)

#spells
count = 0
output_file_path = "Charaters.txt"
with open(output_file_path, "w") as file:
    # Print unique values and write them to the file simultaneously
    print("Unique Values in Column:", Name_Column)
    name_values = df[Name_Column].unique()
    for name in name_values:
        print(name)
        count = count + 1
        file.write(str(name) + "\n")

df = pd.read_csv("DndData/Charaters_unquie.csv")
Name_Column = df.columns[7] #names column



# #class abilites
# output_file_path = "AbilitiesOutput.txt"
# with open(output_file_path, "w") as file:
#     for ability in abilities:
#         print(ability)
#         file.write(str(ability) + "\n")
