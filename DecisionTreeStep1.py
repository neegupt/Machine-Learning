
from random import randint
import random

n=10

Depth=3

data = []
# random.seed("SamTopNeelBottom")
for j in range (0,100):
    new_list = []
    for i in range (0,n):
        new_list.append(randint(0,1))
    data.append(new_list)
# print (data)

final = []
order = []
def strength(points, level, exclude):
    excluded = []
    excluded.extend(exclude)
    if level>=Depth:
        final.append([points])
    else:
        featurestrength = [0,0,0,0,0,0,0,0,0,0]

        for j in range (0,len(points)):
            for i in range(1,n):
                if i in excluded:
                    featurestrength[i]=50
                elif (data[j][i]==1 and data[j][0]==1) or (data[j][i]==0 and data[j][0]==0):
                    featurestrength[i]+=1


        optimalfeature = [abs(50-x) for x in featurestrength[1:]].index(max([abs(50-x) for x in featurestrength[1:]]))+1
        datapoint_0=[]
        datapoint_1=[]
        print("optimal", optimalfeature)
        for i in range (0,100):
            if data[i][optimalfeature] == 0:
                datapoint_0.append([data[i]])
            else:
                datapoint_1.append([data[i]])

        excluded.append(optimalfeature)

        order.extend([optimalfeature, featurestrength[optimalfeature]])
        print ("exclude", exclude)


        strength(datapoint_0, level+1, excluded)
        exclude.append(optimalfeature)
        excluded = exclude
        strength(datapoint_1, level+1, excluded)
    


strength(data,0,[])
print final

print order



   
