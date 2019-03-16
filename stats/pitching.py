import pandas as pd
import matplotlib.pyplot as plt

from data import games
#get subset of rows that contain type = "play"
plays = games[games['type'] == 'play']
#Filter for rows that contain strikes - Event = K
strike_outs = plays[plays['event'].str.contains('K')]
#get the number of strikes in each game 
strike_outs = strike_outs.groupby(['year','game_id']).size()
#normalize data
strike_outs = strike_outs.reset_index(name = 'strike_outs')
#convert strike_outs to numeric to plot the graph
strike_outs = strike_outs.loc[:,['year','strike_outs']].apply(pd.to_numeric)
#plot graph
strike_outs.plot(x='year', y='strike_outs', kind='scatter').legend(['Strike Outs'])
plt.show()
