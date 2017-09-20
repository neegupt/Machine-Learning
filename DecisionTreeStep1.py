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


featurestrength = [0,0,0,0,0,0,0,0,0]

for j in range (0,100):
    for i in range(1,10):
        if (data[j][i]==1 and data[j][0]==1) or (data[j][i]==0 and data[j][0]==0):
            featurestrength[i-1]+=1

for i in range (0,9):
    featurestrength[i] = abs(50-featurestrength[i])
    
list1, list2 = (list(x) for x in zip(*sorted(zip(featurestrength, [1,2,3,4,5,6,7,8,9]))))

print list1[::-1], list2[::-1]

