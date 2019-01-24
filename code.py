# --------------
import numpy as np
from collections import Counter
# Not every data format will be in csv there are other file formats also.
# This exercise will help you deal with other file formats and how toa read it.
data_ipl=np.genfromtxt(path,delimiter=",",skip_header=1,dtype=str)


# How many matches were held in total we need to know so that we can analyze further statistics keeping that in mind.
match_code_array=data_ipl[:,0]
num_unique_matches=len(set(match_code_array))
print("the number of unique matches in data set",num_unique_matches)

# this exercise deals with you getting to know that which are all those six teams that played in the tournament.
team1=set(data_ipl[:,3])
team2=set(data_ipl[:,4])
unique=team1.union(team2)
print("the set of all unique teams that plaed ",unique)
# An exercise to make you familiar with indexing and slicing up within data.
extras=data_ipl[:,17]
extras_num=extras.astype(int)
tot_extras=sum(extras_num)
print("the number of extras in all the matches are",tot_extras)


# Get the array of all delivery numbers when a given player got out. Also mention the wicket type.
player_filter=(data_ipl[:,-3]=="SR Tendulakaer")
filtered_ipl=data_ipl[player_filter]
delivery_num=filtered_ipl[:,-12]
wicket_type=filtered_ipl[:,-2]
print("The Number Of Deliverys where Tendulkar Got out are ",delivery_num)
print("the ways Tendulaker got out are",wicket_type)
print(player_filter.shape)
# this exercise will help you get the statistics on one particular team
toss_winner_mask=(data_ipl[:,5]=="mumbai_indians")
toss_winner_data=data_ipl[toss_winner_mask]
unique_matches=set(toss_winner_data[:,0])
num_toss_winner_MI=len(unique_matches)
print("The number of matches MI won the toss are ",num_toss_winner_MI)

# An exercise to know who is the most aggresive player or maybe the scoring player 
in_runs_six=(data_ipl[:,-7]=="6")
data_ipl_filtered=data_ipl[in_runs_six]
batsman_sixes=set(data_ipl_filtered[:,-10])
batsman_count=Counter(batsman_sixes)
print(batsman_count)






