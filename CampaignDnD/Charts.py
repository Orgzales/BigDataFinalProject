import pandas as pd
import numpy as np

df = pd.read_csv("SessionData.csv")
column_names = df.columns.tolist()
print("Column Names:", column_names)
#Column Names: ['Session', 'Character', 'Success Rate (%)']

session_values = df['Session']
character_values = df['Character']
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

print("Top 10 highest success rates for session", session)
for i in range(len(session_data)):
    print(str(i+1) + ": "+ session_data[i][0], session_data[i][1])


# #print each session collection success rates from all charaters in the session
# for file_path in spell_counts_per_file:
#     print("Session: " + str(file_path))
#     charater_success_rates = session_success_rate[file_path]
#     print(charater_success_rates)
#
# #print each sesssion of spells counted for that session
# for file_path in spell_counts_per_file:
#     print("Session: " + str(file_path))
#     print(spell_counts_per_file[file_path])
#
# #print each session of the monsters counted for that session
# for file_path in monster_counts_per_file:
#     print("Session: " + str(file_path))
#     print(monster_counts_per_file[file_path])

#
# # print out the top 10 most common words
# print("!!!!!!!!!!!!!!!!!!!!!!")
# print("Top 10 most common words:")
# for word, count in sorted(word_counts.items(), key=lambda item: item[1], reverse=True)[:10]:
#     print(word + ": " + str(count))
#
# # print out the most successful charaters from sesssion 1
# print("!!!!!!!!!!!!!!!!!!!!!!")
# print("Top 10 most successful characters from session 1:")
# session1 = session_success_rate["crititcalrole/testing\(2x01)_CuriousBeginnings.txt"]
# for character, success_rate in sorted(session1.items(), key=lambda item: item[1], reverse=True)[:10]:
#     print(character + ": " + str(success_rate) + "%")
#
# # print out the most successful charaters from sesssion 2
# print("!!!!!!!!!!!!!!!!!!!!!!")
# print("Top 10 most successful characters from session 2:")
# session2 = session_success_rate["crititcalrole/testing\(2x02)_AShowofScrutiny.txt"]
# for character, success_rate in sorted(session2.items(), key=lambda item: item[1], reverse=True)[:10]:
#     print(character + ": " + str(success_rate) + "%")
#
# # print out the least successful charaters from sesssion 1
# print("!!!!!!!!!!!!!!!!!!!!!!")
# print("Top 10 least successful characters from session 1:")
# for character, success_rate in sorted(session1.items(), key=lambda item: item[1])[:10]:
#     print(character + ": " + str(success_rate) + "%")
#
# # print out the least successful charaters from sesssion 2
# print("!!!!!!!!!!!!!!!!!!!!!!")
# print("Top 10 least successful characters from session 2:")
# for character, success_rate in sorted(session2.items(), key=lambda item: item[1])[:10]:
#     print(character + ": " + str(success_rate) + "%")

# # get the average success rate for each session
# average_success_rate = {}
# count = 0
# for file_path, character_success_rate in session_success_rate.items():
#     count += 1
#     average_success_rate[("Session: " + str(count))] = np.mean(list(character_success_rate.values()))
#
# # # make a line chart for each session and the average success rate
# plt.plot(list(average_success_rate.keys()), list(average_success_rate.values()), label="Average Success Rate")
# plt.xlabel("Session")
# plt.xticks(rotation=45)
# plt.ylabel("Success Rate (%)")
# plt.title("Average Success Rate for Each Session")
# plt.legend()
#
# #get the success rate for charater daf76ff2 from each session and make a line graph
# character_daf76ff2 = {}
# count = 0
# for file_path, character_success_rate in session_success_rate.items():
#     count += 1
#     character_daf76ff2[("Session: " + str(count))] = character_success_rate["daf76ff2"]
#
# class_of_guy = character_classes[character_names.tolist().index("daf76ff2")]
# plt.plot(list(character_daf76ff2.keys()), list(character_daf76ff2.values()), label=("Character: daf76ff2 | " + class_of_guy))
# plt.xlabel("Session")
# plt.xticks(rotation=45)
# plt.ylabel("Success Rate (%)")
# plt.title("Success Rate for Character: daf76ff2")
# plt.legend()
# plt.tight_layout()
#
# plt.savefig("SuccessRate.png")
# plt.show()

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









