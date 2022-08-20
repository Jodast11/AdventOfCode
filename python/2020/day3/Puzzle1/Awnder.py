f = open("Input.txt")
biome = [line.replace("\n","") for line in f]

positionX = 0
right = [1,3,5,7,1]
down = [1,1,1,1,2]

counter = 0
counter_sum = 1
positionY = 0


for i in range(len(right)):     
    while(True):
        if(positionY) >= len(biome):
            break
            
        if biome[positionY][positionX] == "#":
            counter += 1
            
        positionX = (positionX + right[i])%len(biome[0]) 
        positionY = positionY + down[i]
    print(counter)
    counter_sum = counter_sum * counter
    counter = 0
    positionY = 0
    positionX = 0

print("The Final result is: "+str(counter_sum))