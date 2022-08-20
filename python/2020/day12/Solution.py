with open("Input.txt") as f: #open the imput file
    lines = [x for x in f.read().split("\n")] #split its lines and save it into lines
    
#print(lines)

direction = 90
posX=0
posY=0

for i in lines:
    #print(i)
    if "L" in i:
        #print(i[1:4])
        direction -= int(i[1:4])
        if direction<0:
            direction = direction+360
            
    if "R" in i:
        #print(i[1:4])
        direction += int(i[1:4])
        if direction>=360:
            direction = direction-360
            
    if "N" in i:
        posX += int(i[1:4])
        
    if "S" in i:
        posX -= int(i[1:4])
        
    if "E" in i:
        posY += int(i[1:4])
        
    if "W" in i:
        posY -= int(i[1:4])
        
    if "F" in i:
        if direction == 0:
            posX += int(i[1:4]) 
        if direction == 90:
            posY += int(i[1:4])
        if direction == 180:
            posX -= int(i[1:4])
        if direction == 270:
            posY -= int(i[1:4])   
        
    
        
# print(posX)
# print(posY)

print(abs(posX)+abs(posY))