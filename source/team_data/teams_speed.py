import sys
import pandas as pd
import numpy as np
import math

#this file is to add the speed attribute to the team dataset so that we can compare team speeds

data = pd.read_csv('team_data.csv')
data['speed'] = data['player_dist_walk'] / data['player_survive_time']

#read the new team table into the csv file
data.to_csv('team_data2.csv', sep=',')
