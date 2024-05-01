import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


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

#print the highest count of spell form the spells_values
# print(spells_values[0])

#for each session, get the highest number of spells used in the spells_values and print out the name of the spell with the most
for session in session_unqiue_values:
    session_dict = eval(spells_values[session_unqiue_values == session].iloc[0])
    max_spell_count = 0
    spell_name = ""
    for key in session_dict:
        if session_dict[key] > max_spell_count:
            max_spell_count = session_dict[key]
            spell_name = key
    print("Session:", session, spell_name, max_spell_count)

#for first session, take the spells_value and make adictionary, then for next session, take the spells_value and add it to the dictionary
total_spell_count = {}
for i in range(len(session_unqiue_values)):
    session_dict = eval(spells_values[i])
    for key in session_dict:
        if key in total_spell_count:
            total_spell_count[key] += session_dict[key]
        else:
            total_spell_count[key] = session_dict[key]
print(total_spell_count)

#take the total_spell_count and graph it out in a bar chart with the top 10 spells
spell_names = list(total_spell_count.keys())
spell_counts = list(total_spell_count.values())
spell_names = [x for _, x in sorted(zip(spell_counts, spell_names), reverse=True)]
spell_counts = sorted(spell_counts, reverse=True)
spell_names = spell_names[:10]
spell_counts = spell_counts[:10]
colors = cm.viridis(np.linspace(0, 1, 10))

plt.figure(figsize=(15, 10))
bars = plt.bar(spell_names, spell_counts, color=colors)

for bar, count, name in zip(bars, spell_counts, spell_names):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1, f"{count}", ha='center', va='bottom')

plt.xlabel("Spell Name")
plt.gca().xaxis.labelpad = 15.3
plt.ylabel("Number of Times Used")
plt.title("Top 10 Spells Used in All Sessions")
plt.tight_layout()
# plt.savefig("Important_Graphs/Spells_all_sessions.jpeg")
plt.clf()
# plt.show()

df_spells = pd.read_csv("SpellsOutput.csv")
column_names = df_spells.columns.tolist()
print("Column Names:", column_names)
classes_spell_use = df_spells['Classes']
# print(classes_spell_use)

unqiue_classes = ['Artificer', 'Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']


count = 0
for session in session_unqiue_values:
    print(session)
    count += 1
    #in the session, get the highest success rate charater and print out the name of the character + success rate + class
    # session_df = df[df['Session'] == session]
    # max_success_rate = 0
    # character_name = ""
    # for i in range(len(session_df)):
    #     if session_df['Success Rate (%)'].iloc[i] > max_success_rate:
    #         max_success_rate = session_df['Success Rate (%)'].iloc[i]
    #         character_name = session_df['Character'].iloc[i]
    #         character_class = session_df['Character_Class'].iloc[i]
    # print("Session:", session, character_name, max_success_rate, character_class)
    #

    # in the session, get the all characters with the highest success rate and print out the name of the character + success rate + class
    session_df = df[df['Session'] == session]
    success_rate_values = session_df['Success Rate (%)']
    character_values = session_df['Character']
    character_class_values = session_df['Character_Class']
    success_rate_values, character_values, character_class_values = zip(*sorted(zip(success_rate_values, character_values, character_class_values), reverse=True))
    for i in range(len(success_rate_values)):
        #only print if the success rate is greater than 50%
        if success_rate_values[i] > 50:
            print("Session:", session, character_values[i], success_rate_values[i], character_class_values[i])

    if count == 10:
        break


'''
#for each spell in total_spell_count, get the class that uses it the most
spell_class_count = {}
for class_value in unqiue_classes:
    print(class_value)
    spell_class_count[class_value] = 0
    for spell in total_spell_count:
        # print(spell)
        df_spell_class = df_spells[df_spells['Name'] == spell]
        df_spell_class = str(df_spell_class['Classes'])
        # print(df_spell_class)
        if(class_value in df_spell_class):

            # print("yes, " + class_value + " uses " + spell)
            split_number = total_spell_count[spell]
            # print(split_number)
            spell_class_count[class_value] += split_number

print(spell_class_count)

#take the spell_class_count and graph it out in a bar chart with the all classes
class_names = list(spell_class_count.keys())
class_counts = list(spell_class_count.values())
colors = cm.viridis(np.linspace(0, 1, len(class_names)))

class_names = [x for _, x in sorted(zip(class_counts, class_names), reverse=True)]
class_counts = sorted(class_counts, reverse=True)
plt.figure(figsize=(15, 10))
bars = plt.bar(class_names, class_counts, color=colors)



for bar, count, name in zip(bars, class_counts, class_names):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1, f"{count}", ha='center', va='bottom')

plt.xlabel("Class Name")
plt.gca().xaxis.labelpad = 15.3
plt.ylabel("Number of Spells Used")
plt.title("Number of Spells Used by Each Class")
plt.tight_layout()
plt.savefig("Important_Graphs/Spells_Used_classes.jpeg")
# plt.clf()
plt.show()

'''


#for each session, get the highest number of spells used in the spells_values and print out the name of the spell with the most and create its own dictionary
session_spell_count = {}
for session in session_unqiue_values:
    session_dict = eval(spells_values[session_unqiue_values == session].iloc[0])
    max_spell_count = 0
    spell_name = ""
    for key in session_dict:
        if session_dict[key] > max_spell_count:
            max_spell_count = session_dict[key]
            spell_name = key
    session_spell_count[session] = spell_name + ":" + str(max_spell_count)
print(session_spell_count)


#for the average success rate for each session of all characters get the most common class type from unqiue_classes
session_class_count = {}
for session in session_unqiue_values:
    session_dict = eval(spells_values[session_unqiue_values == session].iloc[0])
    max_spell_count = 0
    spell_name = ""
    for key in session_dict:
        if session_dict[key] > max_spell_count:
            max_spell_count = session_dict[key]
            spell_name = key
    session_spell_count[session] = spell_name + ":" + str(max_spell_count)
print(session_spell_count)








'''
#take the session_spell_count and graph it out in a bar chart
session_names = list(session_spell_count.keys())
spell_counts = [int(session_spell_count[session].split(":")[1]) for session in session_names]
spell_names = [session_spell_count[session].split(":")[0] for session in session_names]
colors = cm.viridis(np.linspace(0, 1, len(session_names)))

plt.figure(figsize=(15, 10))
bars = plt.bar(session_names, spell_counts, color=colors)

for bar, count, name in zip(bars, spell_counts, spell_names):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1, f"{count}", ha='center', va='bottom')
    plt.text(bar.get_x() + bar.get_width() / 2, -1.5, f"{name}", ha='center', va='top')

plt.xlabel("Session")
plt.gca().xaxis.labelpad = 15.3
plt.ylabel("Number of Spells Used")
plt.title("Number of Spells Used in Each Session")
plt.tight_layout()
# plt.savefig("Important_Graphs/Spells_all_sessions.jpeg")
# plt.clf()
plt.show()
'''


'''
classes_success_rate = {}
classes_count = {}

for i in range(len(character_class_values)):
    class_name = character_class_values[i]
    if "|" in class_name:
        class_name = "Multi-Class"
    else:
        class_name = class_name.split(" ")[0]
    if class_name in classes_count:
        classes_count[class_name] += 1
        classes_success_rate[class_name] += success_rate_values[i]
    else:
        classes_count[class_name] = 1
        classes_success_rate[class_name] = success_rate_values[i]

for key in classes_count:
    classes_success_rate[key] = classes_success_rate[key] / classes_count[key]
print(classes_success_rate)

classes_success_rate = dict(sorted(classes_success_rate.items(), key=lambda item: item[1], reverse=True))
class_names = list(classes_success_rate.keys())
avg_success_rates = list(classes_success_rate.values())

num_classes = len(class_names)
colors = cm.viridis(np.linspace(0, 1, num_classes))
plt.figure(figsize=(15, 10))
print(class_names)
bars = plt.bar(class_names, avg_success_rates, color=colors)

for bar, rate, class_name in zip(bars, avg_success_rates, class_names):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1, f"{rate:.2f}%", ha='center', va='bottom')
    plt.text(bar.get_x() + bar.get_width() / 2, -1.5, f"{classes_count[class_name]}", ha='center', va='top')

plt.xlabel("Classes + Count of Characters with class")
plt.gca().xaxis.labelpad = 15.3
plt.ylabel("Average Success Rate for all Characters Classes")
plt.title("Average Success Rate for Each Class for ALL sessions")
# plt.xticks(rotation=45)  # Rotate x-axis labels for readability
plt.tight_layout()  # Ensure a tidy layout
plt.savefig("Important_Graphs/Classes_all_sessions.jpeg")
plt.clf()
# plt.show()  # Display the plot

# Iterate over each unique session to create a separate graph
for session_name in session_values:
    print("Session:", session_name)
    session_df = df[df['Session'] == session_name]
    classes_count = {}
    classes_success_rate = {}

    for i in range(len(session_df)):
        class_name = session_df['Character_Class'].iloc[i]
        if "|" in class_name:
            class_name = "Multi-Class"
        else:
            class_name = class_name.split(" ")[0]

        if class_name in classes_count:
            classes_count[class_name] += 1
            classes_success_rate[class_name] += session_df['Success Rate (%)'].iloc[i]
        else:
            classes_count[class_name] = 1
            classes_success_rate[class_name] = session_df['Success Rate (%)'].iloc[i]

    for key in classes_count:
        classes_success_rate[key] = classes_success_rate[key] / classes_count[key]

    classes_success_rate = dict(sorted(classes_success_rate.items(), key=lambda item: item[1], reverse=True))
    class_names = list(classes_success_rate.keys())
    avg_success_rates = list(classes_success_rate.values())
    num_classes = len(class_names)
    colors = cm.viridis(np.linspace(0, 1, num_classes))

    plt.figure(figsize=(15, 10))
    bars = plt.bar(class_names, avg_success_rates, color=colors)

    for bar, rate, class_name in zip(bars, avg_success_rates, class_names):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1, f"{rate:.2f}%", ha='center', va='bottom')
        plt.text(bar.get_x() + bar.get_width() / 2, -1.5, f"{classes_count[class_name]}", ha='center', va='top')

    session_name = session_name[session_name.find("_")+1:session_name.find(".")]
    # print("Session:", session_name)
    plt.xlabel("Classes + Count of Characters with class")
    plt.gca().xaxis.labelpad = 15.3
    plt.ylabel("Average Success Rate for all Characters Classes")
    plt.title("Average Success Rate for Each Class in Session" + session_name)
    # plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("Classes_SuccessRates/Classes_" + session_name + ".jpeg")
    plt.clf()

    # Show the plot for this session
    # plt.show()
'''

#for each session, get the highest number of spells used in the spells_values


# plt.figure(figsize=(18, 9), dpi=300)
# get the average success rate for each session of all characters and graph it out in a line chart
# sessions = session_values.unique() #get all unique sessions file names
# average_success_rate_session = {}
# list_of_shorten_session = []
# count = 0
# for session in sessions:
#     session_data = []
#     count = count + 1
#     for i in range(len(session_values)):
#         if session_values[i] == session:
#             session_data.append(success_rate_values[i])
#     average_success_rate = np.mean(session_data)
#     session = session[session.find("_")+1:session.find(".")] #change the x to be only the first 7 chars between a splice of "_" and "."
#     session = session[:10] + "..."
#     # list_of_shorten_session.append(session)
#     list_of_shorten_session.append(count)
#     average_success_rate_session[session] = average_success_rate
#     print("Average success rate for session", session, "is", average_success_rate)
#     if count == 30:
#         break
#
# plt.plot(list_of_shorten_session, list(average_success_rate_session.values()), linestyle=':', color='black', label="Average Success Rate")
# plt.xlabel("Session #")
# # plt.xticks(rotation=45)
# tick_locations = np.arange(0, 10, 1)
# plt.xticks(tick_locations)
# plt.ylabel("Success Rate (%)")
# plt.title("Average Success Rate for Each Session")
# plt.legend()
# plt.tight_layout()

#take this line graph and see if there is a word "boss" in the session words for that session, if there is add a point in the line graph for that session
# Get unique sessions and initialize variables
# sessions = session_values.unique()
# average_success_rate_session = {}
# list_of_shorten_session = []
# session_contains_boss = []
# count = 0
#
# # Calculate average success rate for each session
# for session in sessions:
#     session_data = []
#     count += 1
#     # Collect success rates for the current session
#     session_indices = (session_values == session)
#     session_data = success_rate_values[session_indices]
#
#     average_success_rate = np.mean(session_data)
#
#     # Shorten session name for display
#     shortened_session = session[session.find("_") + 1:session.find(".")]
#     shortened_session = shortened_session[:10] + "..."
#
#     list_of_shorten_session.append(count)
#     average_success_rate_session[shortened_session] = average_success_rate
#
#     # Check if "boss" is in the Words for this session
#     words_match = words_values[session_unqiue_values == session]
#     is_boss_present = False
#
#     if not words_match.empty:
#         words_for_session = words_match.iloc[0].lower()
#         if "boss" in words_for_session:
#             session_contains_boss.append(count)
#             is_boss_present = True
#
#     print("Average success rate for session", shortened_session, "is", average_success_rate)
#
#     if count == 30:
#         break
#
# # Create a list of bar colors based on the presence of "boss"
# bar_colors = ['red' if count in session_contains_boss else 'black' for count in list_of_shorten_session]
#
# # Create a bar chart for the average success rates
# # plt.figure(figsize=(18, 9), dpi=300)
# plt.bar(list_of_shorten_session, list(average_success_rate_session.values()), color=bar_colors)
#
# # Chart customization
# plt.xlabel("Session #")
# plt.xticks(np.arange(1, 31, 1))  # Adjusted to match count-based indexing
# plt.ylabel("Success Rate (%)")
# plt.title("Average Success Rate for Each Session")
#
# # Tight layout and display
# plt.tight_layout()
# plt.show()
#
