import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

data = pd.read_csv('aggregate_data.csv')


#all of these uses the groupby function so that we can identify all the unique team id's so that we
#can find all the team kills and distance traveled and things like that
game_size = data.groupby(['match_id','team_id'])[['game_size']].mean()
party_size = data.groupby(['match_id','team_id']).size()
player_dist_ride = data.groupby(['match_id','team_id'])[['player_dist_ride']].mean()
player_dist_walk = data.groupby(['match_id','team_id'])[['player_dist_walk']].mean()
player_survive_time = data.groupby(['match_id', 'team_id'])[['player_survive_time']].mean()
player_kills = data.groupby(['match_id','team_id'])[['player_kills']].sum()
team_placement = data.groupby(['match_id','team_id'])[['team_placement']].mean()

#concat all of the dataframes together so that it is in one table
result = pd.concat([game_size, party_size, player_dist_ride, player_dist_walk, player_survive_time, player_kills, team_placement], axis=1)

#reset the index so that it looks nicely
#new_data = (result.reset_index()[['match_id', 'team_id', 'game_size', 'party_size', 'player_dist_ride', 'player_dist_walk', 'player_kills', 'team_placement']])


#read the new team table into the csv file
result.to_csv('team_data.csv', sep=',')
