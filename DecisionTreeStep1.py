from random import randint
import random

n=10

data = []
# random.seed("SamTopNeelBottom")
for j in range (0,100):
    new_list = []
    for i in range (0,n):
        new_list.append(randint(0,1))
    data.append(new_list)
# print (data)


featurestrength = [0,0,0,0,0,0,0,0,0,0]

for j in range (0,100):
    for i in range(1,n):
        if (data[j][i]==1 and data[j][0]==1) or (data[j][i]==0 and data[j][0]==0):
            featurestrength[i]+=1

for i in range (1,n):
    featurestrength[i] = abs(50-featurestrength[i])

optimalfeature = featurestrength.index(max(featurestrength)
 
datasplit_1 = []
datasplit_2 = []

for i in range(0,100):
    if data[i][optimalfeature] == 1:
        datasplit_1_1.append[data[i]]
    else:
        datasplit_1_2.append[data[i]]
        
