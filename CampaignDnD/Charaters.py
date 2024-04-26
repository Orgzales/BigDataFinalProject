import pandas as pd
import csv

df = pd.read_csv("DndData/Charaters.csv")
# df = pd.read_csv("DndData/Charaters_unquie.csv")

#pulling data that is useful only for the characters
column_names = df.columns.tolist()
#[' ip', 'finger', 'hash', 'name', 'race', 'background', 'date', 'class', 'justClass', 'subclass',
# 'level', 'feats', 'HP', 'AC', 'Str', 'Dex', 'Con', 'Int', 'Wis', 'Cha', 'alignment', 'skills', 'weapons',
# 'spells', 'castingStat', 'choices', 'country', 'countryCode', 'processedAlignment', 'good', 'lawful',
# 'processedRace', 'processedSpells', 'processedWeapons', 'alias']
print("Column Names:", column_names)


name_values = df['name']
class_values = df['class']
spells_values = df['spells']
skills_values = df['skills']

#spells label "nan" replace it with "No spells"
for i in range(len(spells_values)):
    if spells_values[i] != spells_values[i]:
        spells_values[i] = "No spells"

#names label "nan" replace it with "No name"
for i in range(len(name_values)):
    if name_values[i] != name_values[i]:
        name_values[i] = "No name from Charater #" + str(i)

#skills label "nan" replace it with "No skills"
for i in range(len(skills_values)):
    if skills_values[i] != skills_values[i]:
        skills_values[i] = "No skills"

#FOR SOME REASON IS NOT WORKING
#spells label "nan" replace it with "No spells"
# df['spells'] = df['spells'].fillna("No spells")
#
# #names label "nan" replace it with "No name"
# df['name'] = df.index.apply(lambda x: "No name from Charater #" + str(x) if pd.isna(df['name'][x]) else df['name'][x])
#
#
# #skills label "nan" replace it with "No skills"
# df['skills'] = df['spells'].fillna("No spells")

count = 0
output_file_path = "Charaters.csv"

with open(output_file_path, "w", newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Name", "Class", "Spells", "Skills"])  # Header
    for name in name_values:
        if count >= 1000:  # testing
            break
        print(name)
        csv_writer.writerow([name, class_values[count], spells_values[count], skills_values[count]])
        count += 1
