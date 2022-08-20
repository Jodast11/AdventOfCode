lines = [x.strip() for x in open("input.txt")][0].split(", ")

def rotate(direction, currentrotation):
    if direction == "L":
        newrotation = currentrotation - 1
        if newrotation < 0:
            newrotation = 3
        return newrotation
    else:
        newrotation = currentrotation + 1
        if newrotation > 3:
            newrotation = 0
        return newrotation

rotation = 0

posHor = 0
posVer = 0

for line in lines:
    rotation = rotate(line[0], rotation)
    if rotation == 0:
        posHor += int(line[1:])
    if rotation == 2:
        posHor -= int(line[1:])
    if rotation == 1:
        posVer += int(line[1:])
    if rotation == 3:
        posVer -= int(line[1:])

print(abs(posHor)+abs(posVer))