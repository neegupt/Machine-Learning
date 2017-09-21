from random import randint
import random

n=10

Depth=3

data = []
# random.seed("SamTopNeelBottom")
# Generate data for decision tree
for j in range (0,100):
    new_list = []
    for i in range (0,n):
        new_list.append(randint(0,1))
    data.append(new_list)
# print (data)

final = []
order = []

# Calculate the strength of different features and sort the data into subgroups
def strength(points, level, exclude):
    excluded = []
    excluded.extend(exclude)
    if level>=Depth:
        final.append([points])
    else:
        featurestrength = [0,0,0,0,0,0,0,0,0,0]

      	print ("points", points)

        for j in range (0,len(points)):
            for i in range(1,n):
            	# check if feature has been used in branch before
            	print j,i
                if i in excluded:
                    featurestrength[i]=50
                elif (points[j][i]==1 and points[j][0]==1) or (points[j][i]==0 and points[j][0]==0):
                    featurestrength[i]+=1
        # calculate the optimal feature
        optimalfeature = [abs(50-x) for x in featurestrength[1:]].index(max([abs(50-x) for x in featurestrength[1:]]))+1
        datapoint_0=[]
        datapoint_1=[]
        print("optimal", optimalfeature)
        for i in range (0,len(points)):
            if points[i][optimalfeature] == 0:
                datapoint_0.append(points[i])
            else:
                datapoint_1.append(points[i])

        excluded.append(optimalfeature)

        order.extend([optimalfeature, featurestrength[optimalfeature]])
        print ("exclude", exclude)

        # run the function on the two new subgroups
        strength(datapoint_0, level+1, excluded)
        exclude.append(optimalfeature)
        excluded = exclude
        strength(datapoint_1, level+1, excluded)
    


strength(data,0,[])
print final

print order
