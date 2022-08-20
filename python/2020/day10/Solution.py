import time

with open("Input.txt") as f:
    data_cleaned = [int(x) for x in f.read().split("\n")]

data_cleaned.append(0)
data_cleaned.append(max(data_cleaned)+3) #add the last device
data_cleaned.sort()

paths = [0] * (max(data_cleaned)+1) #make array with all zeros and the length of the highest value of data_cleaned and 1
paths[0] = 1 #set value 0 in array paths to zero
#print(paths)

for index in range(1,max(data_cleaned)+1): #make a loop where index is incrementet from 1 to the length of data_cleaned
    for x in range(1,4): #make a loop wher i is 1 to 3
        if (index-x) in data_cleaned: #see if a valid number is in data cleaned
            paths[index] += paths[index - x] #add the previous value to paths at position index

print(paths)
print(paths[-1])

#print(max(data_cleaned))



    