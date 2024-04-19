import pandas as pd

df = pd.read_csv("DndData/dnd-spells.csv")
Name_Column = df.columns[0] #names column
# first_ROW = df.iloc[0].tolist()


column_names = df.columns.tolist()
print("Column Names:", column_names)

# print("first Row:", first_ROW)
print("Column: " + Name_Column)

output_file_path = "SpellsOuput.txt"
with open(output_file_path, "w") as file:
    # Print unique values and write them to the file simultaneously
    print("Unique Values in Column:", Name_Column)
    name_values = df[Name_Column].unique()
    for name in name_values:
        print(name)
        file.write(str(name) + "\n")

print("Output written to:", output_file_path)

#LATER ON ADD CLASS ABILITIES TO THE SPELLS