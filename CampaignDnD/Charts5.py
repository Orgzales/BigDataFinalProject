import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns
import matplotlib.colors as mcolors
named_colors = list(mcolors.CSS4_COLORS.keys())
print(named_colors)


df_counts = pd.read_csv("SessionDataCounts.csv")
column_names = df_counts.columns.tolist()
print("Column Names:", column_names)
#Column Names: ['Session', 'Spells', 'Monsters', 'Words', 'Level_up']

session_unqiue_values = df_counts['Session']
spells_values = df_counts['Spells']
monsters_values = df_counts['Monsters']
words_values = df_counts['Words']
level_up_values = df_counts['Level_up']

df = pd.read_csv("SessionData.csv")
column_names = df.columns.tolist()
print("Column Names:", column_names)
#Column Names: ['Session', 'Character', 'Character_Class', 'Success Rate (%)']

session_values = df['Session'].unique()
character_values = df['Character']
character_class_values = df['Character_Class']
success_rate_values = df['Success Rate (%)']

df_spells = pd.read_csv("SpellsOutput.csv")
column_names = df_spells.columns.tolist()
classes_spell_use = df_spells['Classes']

unqiue_classes = ['Artificer', 'Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']

#testing 1
classes = []
for class_name in character_class_values:
    class_combo = []
    split_strings = class_name.split("|")
    for CLASS in split_strings:
        split_name1 = CLASS.split(" ")[0]
        class_combo.append(split_name1)
    classes.append(class_combo)

print(classes)

#testing 2
monk_count = {}
for class_name in unqiue_classes:
    count = 0
    for class_combo in classes:
        if "Monk" in class_combo and class_name in class_combo:
            count += 1
    monk_count[class_name] = count
print(monk_count)

# Testing 3
monk_success_rate = {}
for class_name in unqiue_classes:
    count = 0
    success_rate = 0
    for i in range(len(classes)):
        if "Monk" in classes[i] and class_name in classes[i]:
            count += 1
            success_rate += success_rate_values[i]
    if count != 0:
        monk_success_rate[class_name] = round(success_rate/count, 2)
    else:
        monk_success_rate[class_name] = 0
print(monk_success_rate)

#Getting each of all combinations of classes with classes
class_success_rate = {}
for class_name in unqiue_classes:
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(class_name)
    class_rate = {}
    for class_name2 in unqiue_classes:
        if class_name == class_name2:
            class_rate[class_name2] = 0
            continue
        count = 0
        success_rate = 0
        for i in range(len(classes)):
            if class_name in classes[i] and class_name2 in classes[i]:
                count += 1
                success_rate += success_rate_values[i]
        if count != 0:
            class_rate[class_name2] = round(success_rate/count, 2)
        else:
            class_rate[class_name2] = 0
    class_success_rate[class_name] = class_rate
    for key, value in class_rate.items():
        if key == class_name:
            class_rate[key] = 0
            continue
        if value == 0:
            class_rate[key] = round(sum(class_rate.values())/len(class_rate), 2)
    print(class_name2 + ":" + str(class_rate))


print(class_success_rate)

df_heatmap = pd.DataFrame(class_success_rate)
# df_heatmap.fillna(success_rate_values.mean(), inplace=True)  # Default is axis=0, i.e., fill by column mean
df_heatmap_transposed = df_heatmap.transpose()
print(df_heatmap)
print(df_heatmap_transposed)

colors = [
    (0, "red"),
    (0.3, "orange"),
    (0.5, "yellow"),
    (0.7, "yellowgreen"),
    (1, "green"),
]

custom_cmap = LinearSegmentedColormap.from_list("custom_cmap", colors)
mask = df_heatmap_transposed == 0.00

plt.figure(figsize=(15, 15))
heatmap = sns.heatmap(
    df_heatmap_transposed,
    annot=True,  # Annotate the heatmap with values
    fmt=".2f",  # Format with 2 decimal places
    cmap=custom_cmap,  # Use the custom colormap
    cbar=True,  # Include a color bar
    mask=mask,  # Apply the mask to black out specific cells
)

plt.title("Multi-Class Success Rate Chart")
plt.xlabel("Primary D&D Classes")
plt.ylabel("Secondary D&D Classes")
# plt.xticks(rotation=45)
plt.tight_layout()
# plt.show()
plt.savefig("MultiClass_SuccessRates.png")
plt.clf()
