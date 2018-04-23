import sys
import pandas as pd
import numpy as np
import math
from matplotlib import pyplot as plt

#this file is just to visualize if the amount of kills a team has is correlated to the placement they got

data = pd.read_csv('../team_data/team_data3.csv')

f1 = data['player_kills'].values
f2 = data['team_placement'].values
plt.scatter(f1, f2, c='black', s=7)
plt.xlabel("Team Kills")
plt.ylabel("Team Placement")
plt.title("Teams Kills vs Team Placement")
plt.show()
