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
