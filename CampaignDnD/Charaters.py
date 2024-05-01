import pandas as pd
import csv
import numpy as np

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

#spells label is empty replace it with "No spells"
df['spells'].fillna('No spells', inplace=True)

#names label "nan" replace it with "No name"
df['name'].replace('', np.nan, inplace=True)
for i in range(len(df['name'])):
    if pd.isna(df['name'].iloc[i]):  # Checks if it's NaN
        df.loc[i, 'name'] = "No name from Character #" + str(i)

#skills label "nan" replace it with "No skills"
df['skills'].fillna('No skills', inplace=True)

count = 0
output_file_path = "Charaters.csv"

with open(output_file_path, "w", newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Name", "Class", "Spells", "Skills"])  # Header
    for name in name_values:
        # if count >= 5:  # testing
        #     break
        print(name)
        csv_writer.writerow([name, class_values[count], spells_values[count], skills_values[count]])
        count += 1
