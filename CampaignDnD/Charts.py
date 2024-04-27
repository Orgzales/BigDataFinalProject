import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("SessionData.csv")
column_names = df.columns.tolist()
print("Column Names:", column_names)
#Column Names: ['Session', 'Character', 'Character_Class', 'Success Rate (%)']

session_values = df['Session']
character_values = df['Character']
character_class_values = df['Character_Class']
success_rate_values = df['Success Rate (%)']


# for each session, find the top 10 highest success rates of characters and print them out neatly sorted
sessions = session_values.unique() #get all unique sessions file names
for session in sessions:
    session_data = []
    for i in range(len(session_values)):
        if session_values[i] == session:
            session_data.append([character_values[i], success_rate_values[i]])
    session_data = sorted(session_data, key=lambda x: x[1], reverse=True)
    session_data = session_data[:10]
    print("Top 10 highest success rates for session", session)
    for i in range(len(session_data)):
        print(str(i+1) + ": "+ session_data[i][0], session_data[i][1])

# for each session, find the top 10 lowest success rates of characters and print them out neatly sorted
sessions = session_values.unique() #get all unique sessions file names
for session in sessions:
    session_data = []
    for i in range(len(session_values)):
        if session_values[i] == session:
            session_data.append([character_values[i], success_rate_values[i]])
    session_data = sorted(session_data, key=lambda x: x[1])
    session_data = session_data[:10]
    print("Top 10 lowest success rates for session", session)
    for i in range(len(session_data)):
        print(str(i+1) + ": "+ session_data[i][0], session_data[i][1])

plt.figure(figsize=(18, 9), dpi=300)
# get the average success rate for each session of all characters and print it out
sessions = session_values.unique() #get all unique sessions file names
average_success_rate_session = {}
list_of_shorten_session = []
count = 0
for session in sessions:
    session_data = []
    count = count + 1
    for i in range(len(session_values)):
        if session_values[i] == session:
            session_data.append(success_rate_values[i])
    average_success_rate = np.mean(session_data)
    session = session[session.find("_")+1:session.find(".")] #change the x to be only the first 7 chars between a splice of "_" and "."
    session = session[:10] + "..."
    # list_of_shorten_session.append(session)
    list_of_shorten_session.append(count)
    average_success_rate_session[session] = average_success_rate
    print("Average success rate for session", session, "is", average_success_rate)

# make a line chart for each session and the average success rate

plt.plot(list_of_shorten_session, list(average_success_rate_session.values()), linestyle=':', color='black', label="Average Success Rate")
plt.xlabel("Session #")
# plt.xticks(rotation=45)
tick_locations = np.arange(0, 110, 5)
plt.xticks(tick_locations)
plt.ylabel("Success Rate (%)")
plt.title("Average Success Rate for Each Session")
plt.legend()
# plt.show()
# plt.tight_layout()

character_names = df['Character'].unique()
# #get the success rate for charaters {num} from each session and make a line graph
for character in character_names[:10]:
    character_data = {}
    # print("name: " + character)
    for i in range(len(character_values)):
        if character_values[i] == character:
            character_data[session_values[i]] = success_rate_values[i]
            # print("Success rate for character", character, "in session", session_values[i], "is", success_rate_values[i])
    session = session[session.find("_")+1:session.find(".")] #change the x to be only the first 7 chars between a splice of "_" and "."
    character_label = character + ": " + character_class_values[character_values.tolist().index(character)]
    plt.plot(list_of_shorten_session, list(character_data.values()), label=character_label)
plt.xlabel("Session #")
# plt.xticks(rotation=45)
tick_locations = np.arange(0, 110, 5)
plt.xticks(tick_locations)
plt.ylabel("Success Rate (%)")
plt.title("Success Rate for Characters #1-10")
plt.legend()
# plt.tight_layout()
# plt.savefig("Graphs_and_Charts/First10Charaters.jpeg")
plt.show()
plt.clf()

#  10 highest averages from each session
for session in sessions:
    plt.figure(figsize=(18, 9), dpi=300)
    plt.title("Success Rate for the 10 Highest Averages in Session " + session)
    session_data = []
    for i in range(len(session_values)):
        if session_values[i] == session:
            session_data.append([character_values[i], success_rate_values[i]])
    session_data = sorted(session_data, key=lambda x: x[1], reverse=True)
    session_data = session_data[:10]
    for i in range(len(session_data)):
        character = session_data[i][0]
        character_data = {}
        for i in range(len(character_values)):
            if character_values[i] == character:
                character_data[session_values[i]] = success_rate_values[i]
        session = session[session.find("_")+1:session.find(".")] #change the x to be only the first 7 chars between a splice of "_" and "."
        character_label = character + ": " + character_class_values[character_values.tolist().index(character)]
        plt.plot(list_of_shorten_session, list(character_data.values()), label=character_label)
    plt.plot(list_of_shorten_session, list(average_success_rate_session.values()), linestyle=':', color='black', label="Average Success Rate")
    plt.xlabel("Session")
    # plt.xticks(rotation=45)
    tick_locations = np.arange(0, 110, 5)
    plt.xticks(tick_locations)
    plt.ylabel("Success Rate (%)")
    plt.legend()
    plt.tight_layout()
    plt.show()
    # plt.savefig("AllSession_Charts/" + session + "_10highest.jpeg")
    plt.clf()

# # success rate for the 10 lowest averages from each session
for session in sessions:
    plt.figure(figsize=(18, 9), dpi=300)
    plt.title("Success Rate for the 10 Lowest Averages in Session " + session)
    session_data = []
    for i in range(len(session_values)):
        if session_values[i] == session:
            session_data.append([character_values[i], success_rate_values[i]])
    session_data = sorted(session_data, key=lambda x: x[1])
    session_data = session_data[:10]
    for i in range(len(session_data)):
        character = session_data[i][0]
        character_data = {}
        for i in range(len(character_values)):
            if character_values[i] == character:
                character_data[session_values[i]] = success_rate_values[i]
        session = session[session.find("_")+1:session.find(".")] #change the x to be only the first 7 chars between a splice of "_" and "."
        character_label = character + ": " + character_class_values[character_values.tolist().index(character)]
        plt.plot(list_of_shorten_session, list(character_data.values()), label=character_label)
    plt.plot(list_of_shorten_session, list(average_success_rate_session.values()), linestyle=':', color='black', label="Average Success Rate")
    plt.xlabel("Session")
    # plt.xticks(rotation=45)
    tick_locations = np.arange(0, 110, 5)
    plt.xticks(tick_locations)
    plt.ylabel("Success Rate (%)")
    plt.legend()
    # plt.tight_layout()
    plt.show()

    # plt.savefig("AllSession_Charts/" + session + "_10lowest.jpeg")
    plt.clf()

#First 500 charaters for all sessions in 10 charater increments
fileCount = 1
for i in range(0, len(character_names), 10):
    plt.figure(figsize=(18, 9), dpi=300)
    for character in character_names[i:i+10]:
        character_data = {}
        print("name: " + character)
        for i in range(len(character_values)):
            if character_values[i] == character:
                character_data[session_values[i]] = success_rate_values[i]
                # print("Success rate for character", character, "in session", session_values[i], "is", success_rate_values[i])
        session = session[session.find("_")+1:session.find(".")] #change the x to be only the first 7 chars between a splice of "_" and "."
        character_label = character + ": " + character_class_values[character_values.tolist().index(character)]
        plt.plot(list_of_shorten_session, list(character_data.values()), label=character_label)
    plt.plot(list_of_shorten_session, list(average_success_rate_session.values()), linestyle=':', color='black', label="Average Success Rate")
    plt.xlabel("Session")
    # plt.xticks(rotation=45)
    tick_locations = np.arange(0, 110, 5)
    plt.xticks(tick_locations)
    plt.ylabel("Success Rate (%)")
    plt.title("Success Rate for Characters #" + str(fileCount) + "-" + str(fileCount+10))
    plt.legend()
    # plt.savefig("Graphs_and_Charts/First500Charaters_" + str(fileCount) + "-" + str(fileCount+10) + ".jpeg")
    # plt.tight_layout()
    plt.show()
    plt.clf()
    fileCount += 10
    print("file printed fr charaters range: " + str(fileCount))
    if i == 50:
        break












