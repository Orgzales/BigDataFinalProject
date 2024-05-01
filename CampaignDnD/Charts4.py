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

#get the average success rate for all classes that have  "Wizard 2" in their class
wizard_2 = df.loc[df['Character_Class'] == "Wizard 2"]
print(wizard_2)
wizard_2_average = wizard_2['Success Rate (%)'].mean()
print(wizard_2_average)

#get the average success rate for each level of wizard from 1 to 20 in their class
wizard_level = {}
for i in range(1, 21):
    wizard_level[i] = df.loc[df['Character_Class'] == "Wizard " + str(i)]
    wizard_level[i] = wizard_level[i]['Success Rate (%)'].mean()
print(wizard_level)

#get the average success rate for each class in the unqiue_classes list from 1 to 20 in their class
classes_avg_rate = {}
for class_name in unqiue_classes:
    class_level = {}
    for i in range(1, 21):
        class_level[i] = df.loc[df['Character_Class'] == class_name + " " + str(i)]
        class_level[i] = class_level[i]['Success Rate (%)'].mean()
        class_level[i] = round(class_level[i], 2)
    print(class_name, class_level)
    classes_avg_rate[class_name] = class_level


#make a heatmap of the class success rate for each levels
df_heatmap = pd.DataFrame(classes_avg_rate)
df_heatmap.fillna(df_heatmap.mean(), inplace=True)
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

plt.figure(figsize=(15, 15))
heatmap = sns.heatmap(
    df_heatmap_transposed,
    annot=True,  # Annotate the heatmap with values
    fmt=".2f",  # Format as integers
    cmap=custom_cmap,  # Use the custom colormap
    cbar=True,  # Include a color bar
    # vmin=0,  # Minimum value for the colormap
    # vmax=20,  # Maximum value for the colormap (colors capped at 5)
)

plt.title("Class Level Success Rate")
plt.xlabel("Level")
plt.ylabel("D&D Classes")
# plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# plt.savefig("LevelsandSuccessrates.png")
plt.clf()




# finding all the count of spells for each class in each session
#
# list_of_classes = {}
# count = 0
# for dict in list_of_sessions:
#     # print(dict)
#     count += 1
#     for class_value in unqiue_classes:
#         # print(class_value)
#         class_dict = {}
#         # spell_count = 0
#         for spell in list_of_sessions[dict]:
#             # print(spell)
#             df_spell_class = df_spells[df_spells['Name'] == spell]
#             df_spell_class = str(df_spell_class['Classes'])
#             # print(df_spell_class)
#             if(class_value in df_spell_class):
#                 class_dict[spell] = list_of_sessions[dict][spell]
#             # spell_count += 1
#             # if(spell_count > 25):
#             #     break
#         list_of_classes[class_value] = class_dict
#     # print(list_of_classes)
#
#     df_heatmap = pd.DataFrame(list_of_classes)
#     df_heatmap = df_heatmap.fillna(0).astype(int)
#     df_heatmap_transposed = df_heatmap.transpose()
#     # print(df_heatmap)
#     # print(df_heatmap_transposed)
#
#
#     colors = [
#         (0, "lightyellow"),
#         (0.3, "yellowgreen"),
#         (0.5, "lightgreen"),
#         (0.7, "green"),
#         (1, "DarkGreen"),
#     ]
#     # colors = [
#     #     (0, "white"),  # Red for low values
#     #     # (0.5, "orange"),  # Orange for middle values
#     #     (1, "green"),  # Green for high values
#     # ]
#     custom_cmap = LinearSegmentedColormap.from_list("custom_cmap", colors)
#
#     # Find columns with a total sum less than 5
#     column_sums = df_heatmap_transposed.sum(axis=0)  # Sum across rows for each column
#     low_sum_columns = column_sums[column_sums < 10].index.tolist()  # Identify low-sum columns
#
#     # Remove columns with a total sum less than 5
#     df_heatmap_transposed = df_heatmap_transposed.drop(columns=low_sum_columns)  # Drop the low-sum columns
#
#     plt.figure(figsize=(10, 10))
#     heatmap = sns.heatmap(
#         df_heatmap_transposed,
#         annot=True,  # Annotate the heatmap with values
#         fmt="d",  # Format as integers
#         cmap=custom_cmap,  # Use the custom colormap
#         cbar=True,  # Include a color bar
#         # vmin=0,  # Minimum value for the colormap
#         # vmax=20,  # Maximum value for the colormap (colors capped at 5)
#     )
#
#     # the spell with the highest total usage
#     column_sums = df_heatmap_transposed.sum(axis=0)
#     max_column = column_sums.idxmax()
#     max_column_index = df_heatmap_transposed.columns.get_loc(max_column)
#     plt.axvline(x=max_column_index + 0.5, color='blue', linewidth=20, alpha=0.1)
#
#     # the class with the highest total spells
#     class_sums = df_heatmap_transposed.sum(axis=1)
#     max_class = class_sums.idxmax()
#     max_class_index = df_heatmap_transposed.index.get_loc(max_class)
#     plt.axhline(y=max_class_index + 0.5, color='blue', linewidth=20, alpha=0.1)
#
#     # Finding all spells with sum under 5
#     low_sum_columns = column_sums[column_sums < 5].index.tolist()
#     for col_name in low_sum_columns:
#         col_index = df_heatmap_transposed.columns.get_loc(col_name)  # Get the column index
#         plt.axvline(x=col_index + 0.5, color='red', linewidth=20, alpha=0.1)
#
#     # Finding all classes with no spell usage
#     rows_with_zeros = df_heatmap_transposed[df_heatmap_transposed.eq(0).all(axis=1)].index.tolist()
#     row_indices = [df_heatmap_transposed.index.get_loc(class_name) for class_name in rows_with_zeros]
#     for row_index in row_indices:
#         plt.axhline(y=row_index + 0.5, color='red', linewidth=20, alpha=0.1)
#
#
#     plt.title("Spell Usage by D&D Classes for " + dict)
#     plt.xlabel("Spells")
#     plt.ylabel("D&D Classes")
#     # plt.xticks(rotation=45)
#     # plt.tight_layout()
#     # plt.show()
#     plt.savefig("HeatMapsBoth/Spell_Usage_by_D&D_Classes_" + str(count) + ".png")
#     plt.clf()
#

