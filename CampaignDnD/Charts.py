import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs


df = pd.read_csv("SessionData.csv")
column_names = df.columns.tolist()
print("Column Names:", column_names)
#Column Names: ['Session', 'Character', 'Character_Class', 'Success Rate (%)']

session_values = df['Session']
character_values = df['Character']
character_class_values = df['Character_Class']
success_rate_values = df['Success Rate (%)']

#Find all charaters + successrates that are from session crititcalrole/testing\(2x01)_CuriousBeginnings.txt and sort them to get the top 10 highest rates
session = "crititcalrole/testing\(2x01)_CuriousBeginnings.txt"
session_data = []
for i in range(len(session_values)):
    if session_values[i] == session:
        session_data.append([character_values[i], success_rate_values[i]])
session_data = sorted(session_data, key=lambda x: x[1], reverse=True)
session_data = session_data[:10]
print(session_data)
#print them out neatly for the user
print("Top 10 highest success rates for session", session)
for i in range(len(session_data)):
    print(str(i+1) + ": "+ session_data[i][0], session_data[i][1])

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


#get the average success rate for "crititcalrole/testing\(2x01)_CuriousBeginnings.txt" of all characters and print it out
session = "crititcalrole/testing\(2x01)_CuriousBeginnings.txt"
session_data = []
for i in range(len(session_values)):
    if session_values[i] == session:
        session_data.append(success_rate_values[i])
average_success_rate = np.mean(session_data)
print("Average success rate for session", session, "is", average_success_rate)

# get the average success rate for each session of all characters and print it out
sessions = session_values.unique() #get all unique sessions file names
average_success_rate_session = {}
list_of_shorten_session = []
for session in sessions:
    session_data = []
    for i in range(len(session_values)):
        if session_values[i] == session:
            session_data.append(success_rate_values[i])
    average_success_rate = np.mean(session_data)
    #change the session key to be only the first 7 chars between a splice of "_" and "."
    session = session[session.find("_")+1:session.find(".")]
    session = session[:7]
    list_of_shorten_session.append(session)
    average_success_rate_session[session] = average_success_rate
    print("Average success rate for session", session, "is", average_success_rate)

# make a line chart for each session and the average success rate
plt.plot(list_of_shorten_session, list(average_success_rate_session.values()), label="Average Success Rate")
plt.xlabel("Session")
plt.xticks(rotation=45)
plt.ylabel("Success Rate (%)")
plt.title("Average Success Rate for Each Session")
plt.legend()
plt.tight_layout()


# #get the success rate for charater daf76ff2 from each session and make a line graph
character = "daf76ff2"
character_data = {}
for i in range(len(character_values)):
    if character_values[i] == character:
        character_data[session_values[i]] = success_rate_values[i]
    #change the x to be only the first 7 chars between a splice of "_" and "."
    session = session[session.find("_")+1:session.find(".")]
print("Success rate for character", character, "in session", session, "is", success_rate_values[i])
character_label = character + ": " + character_class_values[character_values.tolist().index(character)]
plt.plot(list_of_shorten_session, list(character_data.values()), label=character_label)
plt.xlabel("Session")
plt.xticks(rotation=45)
plt.ylabel("Success Rate (%)")
plt.title("Success Rate for Character " + character)
plt.legend()
plt.tight_layout()
plt.show()
plt.clf()


##cluster example

# # Generate synthetic data for clustering
# n_samples = 300
# n_features = 2
# centers = 3
# cluster_std = 1.0
#
# X, y = make_blobs(n_samples=n_samples, n_features=n_features, centers=centers, cluster_std=cluster_std, random_state=42)
#
# # Apply k-means clustering
# n_clusters = 3
# kmeans = KMeans(n_clusters=n_clusters, random_state=42)
# kmeans.fit(X)
#
# # Get the cluster labels and the centroids
# labels = kmeans.labels_
# centroids = kmeans.cluster_centers_
#
# # Plot the clusters and centroids
# plt.figure(figsize=(8, 6))
# for cluster in range(n_clusters):
#     # Plot data points for each cluster
#     plt.scatter(X[labels == cluster][:, 0], X[labels == cluster][:, 1], label=f'Cluster {cluster}', alpha=0.6)
#
# # Plot centroids
# plt.scatter(centroids[:, 0], centroids[:, 1], color='red', label='Centroids', marker='x', s=100)
#
# plt.title('Cluster Chart with K-Means')
# plt.xlabel('Feature 1')
# plt.ylabel('Feature 2')
# plt.legend()
# plt.show()
# plt.clf()
#









