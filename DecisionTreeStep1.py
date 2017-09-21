
from random import randint
import random

n=10

Depth=5

data = []
# random.seed("SamTopNeelBottom")
for j in range (0,100):
    new_list = []
    for i in range (0,n):
        new_list.append(randint(0,1))
    data.append(new_list)
# print (data)

final = []
def strength(points, level):
	if level>=Depth:
		final.append([points])
	else:
		featurestrength = [0,0,0,0,0,0,0,0,0,0]

		for j in range (0,len(points)):
		    for i in range(1,n):
		        if (data[j][i]==1 and data[j][0]==1) or (data[j][i]==0 and data[j][0]==0):
		            featurestrength[i]+=1

		featurestrength2 = featurestrength

		optimalfeature = [abs(50-x) for x in featurestrength[1:]].index(max([abs(50-x) for x in featurestrength[1:]]))+1
		datapoint_1=[]
		datapoint_2=[]
		for i in range (0,100):
			if data[i][optimalfeature] == 0:
				datapoint_1.append([data[i]])
			else:
				datapoint_2.append([data[i]])

		strength(datapoint_1, level+1)
		strength(datapoint_2, level+1)
	

	# print featurestrength[1:]
	# sort stuff here
	# datapoints = subsets of data here


strength(data,0)
print final

	# return featurestrength[optimalfeature]



# if optimalfeature>50:
	
# elif optimalfeature<50:
# 	jgifdkjsg
# else:
# 	continue

        
    
