import sys
import pandas as pd
import numpy as np
import math
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

#100 is not for anything
# cluster_array = [[0.25], [0.5], [0.75], [1], [1.25], [1.5], [1.75], [2], [2.25], [2.5], [2.75], [3]]

data = pd.read_csv('../team_data/team_data3.csv')

#---------------this is us trying to actually implement the kmeans algorithm before we realized
#there was a python libary for it ---------------

# for index, row in data.iterrows():
#     velocity = row['player_dist_walk'] / row['player_survive_time']
#     # closestValue = min(cluster_array, key=lambda x:abs(x - velocity))
#     # closestValue /= 0.25
#
#     min = 100000
#     index = 0
#     for i in cluster_array:
#         value = abs(velocity - i[0])
#
#         if (value < min):
#             min = value
#             index = i[0]
#     temp = (index / 0.25) - 1
#     temp = int(temp)
#     cluster_array[temp].append(velocity)
# print (cluster_array[0])

#need to put just the attributes we need into an array so that we can cluster
dfNew = data[['speed', 'team_placement']]
X = dfNew.as_matrix(columns = None)


#run k means algorithm
kmeans = KMeans(n_clusters=6)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

#plot all the points
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')

centroids = kmeans.cluster_centers_
labels = kmeans.labels_

#plot all the centroids with X's to show where they are at
plt.scatter(centroids[:, 0],centroids[:, 1], marker = "x", s=150, linewidths = 5, zorder = 10)
plt.xlabel("Average Speed of Team")
plt.ylabel("Team Placement")
plt.title("K-Means Algorithm For Average Speed")
plt.show()
