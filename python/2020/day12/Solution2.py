with open("Input.txt") as f: #open the imput file
    lines = [x for x in f.read().split("\n")] #split its lines and save it into lines
    
#print(lines)

posXShip=0
posYShip=0
posXWaypointRel=1
posYWaypointRel=10

for i in lines:
    if "F" in i:
        posXShip += int(i[1:4]) * posXWaypointRel
        posYShip += int(i[1:4]) * posYWaypointRel
    if "N" in i:
        posXWaypointRel += int(i[1:4])
    if "S" in i:
        posXWaypointRel -= int(i[1:4])
    if "E" in i:
        posYWaypointRel += int(i[1:4])
    if "W" in i:
        posYWaypointRel -= int(i[1:4])
    if "L" in i:
        posXWaypointRel_old = posXWaypointRel 
        posYWaypointRel_old = posYWaypointRel
        if int(i[1:4]) == 0:
            posXWaypointRel=posXWaypointRel
            posYWaypointRel=posYWaypointRel
        if int(i[1:4]) == 90:
            posXWaypointRel = posYWaypointRel_old
            posYWaypointRel = -posXWaypointRel_old
        if int(i[1:4]) == 180:
            posXWaypointRel = -posXWaypointRel_old
            posYWaypointRel = -posYWaypointRel_old
        if int(i[1:4]) == 270:
            posXWaypointRel = -posYWaypointRel_old
            posYWaypointRel = posXWaypointRel_old
    if "R" in i:
        posXWaypointRel_old = posXWaypointRel 
        posYWaypointRel_old = posYWaypointRel
        if int(i[1:4]) == 0:
            posXWaypointRel=posXWaypointRel
            posYWaypointRel=posYWaypointRel
        if int(i[1:4]) == 90:
            posXWaypointRel = -posYWaypointRel_old
            posYWaypointRel = posXWaypointRel_old
        if int(i[1:4]) == 180:
            posXWaypointRel = -posXWaypointRel_old
            posYWaypointRel = -posYWaypointRel_old
        if int(i[1:4]) == 270:
            posXWaypointRel = posYWaypointRel_old
            posYWaypointRel = -posXWaypointRel_old
    # print("Ship:")
    # print(posXShip)
    # print(posYShip)
    # print("Waypoint:")
    # print(posXWaypointRel)
    # print(posYWaypointRel)
    
        
# print(posXShip)
# print(posYShip)

print(abs(posXShip)+abs(posYShip))