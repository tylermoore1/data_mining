import sys
import pandas as pd
import numpy as np
import math
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans


data = pd.read_csv('../team_data/team_data3.csv')

# f1 = data['player_kills'].values
# f2 = data['team_placement'].values
# plt.scatter(f1, f2, c='black', s=7)
# plt.show()

def average_placement():
    #------- average placement for certain amount of kills --------

    #index value
    k1 = 0
    k2 = 0
    k3 = 0
    kills = 0
    placement1 = 0
    placement2 = 0
    placement3 = 0
    for index, row in data.iterrows():
        #get number of kills for the team
        kills = row['player_kills']
        #we are using conditional probability to see what the average placement the team finishes in

        #given they have less than 3 kills, what placement would they finish
        if (kills < 3):
            placement1 += row['team_placement']
            k1 += 1
        #same thing with the next two if statements
        elif (kills >= 3 and kills < 8):
            placement2 += row['team_placement']
            k2 += 1
        elif (kills >= 8):
            placement3 += row['team_placement']
            k3 += 1

    #find average placement
    placement1 /= k1
    placement2 /= k2
    placement3 /= k3

    print ("Average Placement for less than 3 kills: " + str(placement1))
    print ("Average Placement for 3 or more kills and less than 8: " + str(placement2))
    print ("Average Placement for 8 or more kills: " + str(placement3) + '\n')

#this function is to see the winning percentage for having a certain number of kills
def win_percentage():
    win1 = 0
    total1 = 0
    win2 = 0
    total2 = 0
    win3 = 0
    total3 = 0
    kills = 0
    placement = 0
    for index, row in data.iterrows():
        kills = row['player_kills']
        placement = row['team_placement']

        #using conditional probability again to see if having less than 3 kills results in getting wins
        if (kills < 3):
            if (placement == 1):
                win1 += 1

            total1 += 1

        #same thing as above, but kills need to be between 3 and 8
        elif (kills >= 3 and kills < 8):
            if (placement == 1):
                win2 += 1

            total2 += 1

        elif (kills >= 8):
            if (placement == 1):
                win3 += 1

            total3 += 1

    #find average winning percentage
    win_percent1 = (win1 / total1) * 100
    win_percent2 = (win2 / total2) * 100
    win_percent3 = (win3  / total3) * 100

    print ("Percentage for first place finish with less than 3 kills: " + str(round(win_percent1, 2)) + '%')
    print ("Percentage for first place finish with 3 or more kills and less than 8: " + str(round(win_percent2, 2)) + '%')
    print ("Percentage for first place finish with more than or equal to 8 kills: " + str(round(win_percent3, 2)) + '%')

def final_percentage():
    kills = 0
    placement = 0
    speed = 0
    win1 = 0
    total1 = 0
    for index, row in data.iterrows():
        kills = row['player_kills']
        placement = row['team_placement']
        speed = row['speed']

        #we are using 1.7 and 2 because from our clustering data, we saw the centroid was around a 1.7 and 2
        #for best placement
        if (kills >= 8 and speed >= 1.8 and speed <= 2.0):
            if (placement == 1):
                win1 += 1

            total1 += 1

    win_percent = (win1 / total1) * 100

    print ("Win Percentage for first place finish with a speed over 1.7 and more than 8 kills: " + str(round(win_percent, 2)) + '%')


#call function function
average_placement()

#call win percentage function
win_percentage()

#now we want to combine our two findings, (a speed of over 2 and more than 8 kills) to see if
#winning percentage goes way up
final_percentage()
