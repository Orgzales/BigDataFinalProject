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

#get the count of all spells from all sessions
total_spell_count = {}
for i in range(len(session_unqiue_values)):
    session_dict = eval(spells_values[i])
    for key in session_dict:
        if key in total_spell_count:
            total_spell_count[key] += session_dict[key]
        else:
            total_spell_count[key] = session_dict[key]
# print(total_spell_count)

# a dictionary that holds dictionaries of all the spells that were used in each session in SessionDataCounts.csv "Spells" column
list_of_sessions = {}
for i in range(len(session_unqiue_values)):
    session_dict = eval(spells_values[i])
    list_of_sessions[session_unqiue_values[i]] = session_dict
# print(list_of_sessions)

for key in list_of_sessions:
    list_of_sessions[key] = {key: value for key, value in list_of_sessions[key].items() if value != 0}
# print(list_of_sessions)

# finding all the count of spells for each class in each session

list_of_classes = {}
count = 0
for dict in list_of_sessions:
    # print(dict)
    count += 1
    for class_value in unqiue_classes:
        # print(class_value)
        class_dict = {}
        # spell_count = 0
        for spell in list_of_sessions[dict]:
            # print(spell)
            df_spell_class = df_spells[df_spells['Name'] == spell]
            df_spell_class = str(df_spell_class['Classes'])
            # print(df_spell_class)
            if(class_value in df_spell_class):
                class_dict[spell] = list_of_sessions[dict][spell]
            # spell_count += 1
            # if(spell_count > 25):
            #     break
        list_of_classes[class_value] = class_dict
    # print(list_of_classes)

    df_heatmap = pd.DataFrame(list_of_classes)
    df_heatmap = df_heatmap.fillna(0).astype(int)
    df_heatmap_transposed = df_heatmap.transpose()
    # print(df_heatmap)
    # print(df_heatmap_transposed)


    colors = [
        (0, "lightyellow"),
        (0.3, "yellowgreen"),
        (0.5, "lightgreen"),
        (0.7, "green"),
        (1, "DarkGreen"),
    ]
    # colors = [
    #     (0, "white"),  # Red for low values
    #     # (0.5, "orange"),  # Orange for middle values
    #     (1, "green"),  # Green for high values
    # ]
    custom_cmap = LinearSegmentedColormap.from_list("custom_cmap", colors)

    # Find columns with a total sum less than 5
    column_sums = df_heatmap_transposed.sum(axis=0)  # Sum across rows for each column
    low_sum_columns = column_sums[column_sums < 10].index.tolist()  # Identify low-sum columns

    # Remove columns with a total sum less than 5
    df_heatmap_transposed = df_heatmap_transposed.drop(columns=low_sum_columns)  # Drop the low-sum columns

    plt.figure(figsize=(10, 10))
    heatmap = sns.heatmap(
        df_heatmap_transposed,
        annot=True,  # Annotate the heatmap with values
        fmt="d",  # Format as integers
        cmap=custom_cmap,  # Use the custom colormap
        cbar=True,  # Include a color bar
        # vmin=0,  # Minimum value for the colormap
        # vmax=20,  # Maximum value for the colormap (colors capped at 5)
    )

    # the spell with the highest total usage
    column_sums = df_heatmap_transposed.sum(axis=0)
    max_column = column_sums.idxmax()
    max_column_index = df_heatmap_transposed.columns.get_loc(max_column)
    plt.axvline(x=max_column_index + 0.5, color='blue', linewidth=20, alpha=0.1)

    # the class with the highest total spells
    class_sums = df_heatmap_transposed.sum(axis=1)
    max_class = class_sums.idxmax()
    max_class_index = df_heatmap_transposed.index.get_loc(max_class)
    plt.axhline(y=max_class_index + 0.5, color='blue', linewidth=20, alpha=0.1)

    # Finding all spells with sum under 5
    low_sum_columns = column_sums[column_sums < 5].index.tolist()
    for col_name in low_sum_columns:
        col_index = df_heatmap_transposed.columns.get_loc(col_name)  # Get the column index
        plt.axvline(x=col_index + 0.5, color='red', linewidth=20, alpha=0.1)

    # Finding all classes with no spell usage
    rows_with_zeros = df_heatmap_transposed[df_heatmap_transposed.eq(0).all(axis=1)].index.tolist()
    row_indices = [df_heatmap_transposed.index.get_loc(class_name) for class_name in rows_with_zeros]
    for row_index in row_indices:
        plt.axhline(y=row_index + 0.5, color='red', linewidth=20, alpha=0.1)


    plt.title("Spell Usage by D&D Classes for " + dict)
    plt.xlabel("Spells")
    plt.ylabel("D&D Classes")
    # plt.xticks(rotation=45)
    # plt.tight_layout()
    # plt.show()
    plt.savefig("HeatMapsBoth/Spell_Usage_by_D&D_Classes_" + str(count) + ".png")
    plt.clf()



#remove any values that are 0 in the total_spell_counts dictionary
total_spell_count = {key: value for key, value in total_spell_count.items() if value != 0}
print(total_spell_count)

#for each spell in total spell counts, find if that class can use them or not and make a new dictionaries of dictionaries that holds all values
list_of_classes = {}
for class_value in unqiue_classes:
    print(class_value)
    class_dict = {}
    # spell_count = 0
    for spell in total_spell_count:
        # print(spell)
        df_spell_class = df_spells[df_spells['Name'] == spell]
        df_spell_class = str(df_spell_class['Classes'])
        # print(df_spell_class)
        if(class_value in df_spell_class):
            class_dict[spell] = total_spell_count[spell]
        # spell_count += 1
        # if(spell_count > 25):
        #     break
    list_of_classes[class_value] = class_dict
print(list_of_classes)



df_heatmap = pd.DataFrame(list_of_classes)
df_heatmap = df_heatmap.fillna(0).astype(int)
print(df_heatmap)
df_heatmap_transposed = df_heatmap.transpose()
print(df_heatmap_transposed)

# Find columns with a total sum less than 5
column_sums = df_heatmap_transposed.sum(axis=0)  # Sum across rows for each column
low_sum_columns = column_sums[column_sums < 1000].index.tolist()  # Identify low-sum columns

# Remove columns with a total sum less than 5
df_heatmap_transposed = df_heatmap_transposed.drop(columns=low_sum_columns)  # Drop the low-sum columns

colors = [
    (0, "white"),  # Red for low values
    # (0.5, "orange"),  # Orange for middle values
    (1, "green"),  # Green for high values
]

custom_cmap = LinearSegmentedColormap.from_list("custom_cmap", colors)



plt.figure(figsize=(8, 6))
heatmap = sns.heatmap(
    df_heatmap_transposed,
    annot=True,  # Annotate the heatmap with values
    fmt="d",  # Format as integers
    cmap=custom_cmap,  # Use the custom colormap
    cbar=True,  # Include a color bar
)

# the spell with the highest total usage
column_sums = df_heatmap_transposed.sum(axis=0)
max_column = column_sums.idxmax()
max_column_index = df_heatmap_transposed.columns.get_loc(max_column)
plt.axvline(x=max_column_index + 0.5, color='blue', linewidth=20, alpha=0.1)

# the class with the highest total spells
class_sums = df_heatmap_transposed.sum(axis=1)
max_class = class_sums.idxmax()
max_class_index = df_heatmap_transposed.index.get_loc(max_class)
plt.axhline(y=max_class_index + 0.5, color='blue', linewidth=20, alpha=0.1)

# Finding all spells with sum under 5
low_sum_columns = column_sums[column_sums < 5].index.tolist()
for col_name in low_sum_columns:
    col_index = df_heatmap_transposed.columns.get_loc(col_name)  # Get the column index
    plt.axvline(x=col_index + 0.5, color='red', linewidth=20, alpha=0.1)

# Finding all classes with no spell usage
rows_with_zeros = df_heatmap_transposed[df_heatmap_transposed.eq(0).all(axis=1)].index.tolist()
row_indices = [df_heatmap_transposed.index.get_loc(class_name) for class_name in rows_with_zeros]
for row_index in row_indices:
    plt.axhline(y=row_index + 0.5, color='red', linewidth=20, alpha=0.1)

# Add labels and titles
plt.title("Spell Usage by D&D Classes")
plt.xlabel("Spells")
plt.ylabel("D&D Classes")

# Show the heatmap
plt.show()
plt.clf()

