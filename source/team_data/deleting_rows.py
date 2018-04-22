import sys
import pandas as pd
import numpy as np
import math

#this file is to delete all rows that have a speed of 0 or bigger than 10. the reason is because when they have
#speed of 0, they didn't even play. Also, no one should have a speed bigger than 10 
data = pd.read_csv('team_data2.csv')
data = data.drop(data[data.speed == 0].index)
data = data.drop(data[data.speed > 10].index)

#read the new team table into the csv file
data.to_csv('team_data3.csv', sep=',')
