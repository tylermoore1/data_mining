import sys
import pandas as pd
import numpy as np
import math
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans


data = pd.read_csv('../team_data/team_data2.csv')

# f1 = data['player_kills'].values
# f2 = data['team_placement'].values
# plt.scatter(f1, f2, c='black', s=7)
# plt.show()

def average_placement():
    #------- this is average placement a team will get with kills less than 3 --------

    #index value
    k = 0
    kills = 0
    placement = 0
    for index, row in data.iterrows():
        kills = row['player_kills']
        if (kills < 3):
            placement += row['team_placement']
            k += 1

    placement /= k

    print ("Average Placement: " + str(placement))

    #------- this is average placement a team will get with kills bigger or equal to 3 and less than 8 --------

    #index value
    k = 0
    kills = 0
    placement = 0
    for index, row in data.iterrows():
        kills = row['player_kills']
        if (kills >= 3 and kills < 8):
            placement += row['team_placement']
            k += 1

    placement /= k

    print ("Average Placement: " + str(placement))

    #------- this is average placement a team will get with kills more than or equal to 8 --------

    #index value
    k = 0
    kills = 0
    placement = 0
    for index, row in data.iterrows():
        kills = row['player_kills']
        if (kills >= 8):
            placement += row['team_placement']
            k += 1

    placement /= k

    print ("Average Placement: " + str(placement))


#call function call
average_placement()
