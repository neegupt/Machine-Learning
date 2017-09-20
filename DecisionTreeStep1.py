from random import randint
import random

data = []
random.seed("SamTopNeelBottom")
for j in range (0,100):
    new_list = []
    for i in range (0,10):
        new_list.append(randint(0,1))
    data.append(new_list)
print (data)


featurestrength = [0,0,0,0,0,0,0,0,0,0]

for j in range (0,100):
    for i in range(0,10):
        (if data[j][i]==1 and data[j][0]==1) or (if data[j][i]==0 and data[j][0]==1):
            featurestrength[i]+=1

    

