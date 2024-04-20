import pandas as pd

abilities = ["Rage", "Bardic Inspiration", "Channel Divinity", "Wild Shape", "Action Surge", "Martial Arts", "Divine Smite",
             "Hunter's Mark", "Sneak Attack", "Metamagic", "Pact Magic", "Arcane Recovery"]

df = pd.read_csv("DndData/dnd-spells.csv")
Name_Column = df.columns[0] #names column
# first_ROW = df.iloc[0].tolist()

column_names = df.columns.tolist()
print("Column Names:", column_names)

# print("first Row:", first_ROW)
print("Column: " + Name_Column)

#spells
output_file_path = "SpellsOuput.txt"
with open(output_file_path, "w") as file:
    # Print unique values and write them to the file simultaneously
    print("Unique Values in Column:", Name_Column)
    name_values = df[Name_Column].unique()
    for name in name_values:
        print(name)
        file.write(str(name) + "\n")

#class abilites
output_file_path = "AbilitiesOutput.txt"
with open(output_file_path, "w") as file:
    for ability in abilities:
        print(ability)
        file.write(str(ability) + "\n")
