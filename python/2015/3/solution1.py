import os

with open(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt", "r") as f:
    lines = [x for x in f.read().split("\n")[0]]

locationsVisited = []
countDifferentLocations = 0

xPos = 0
yPos = 0
posStr = str(xPos)+str(yPos)
countDifferentLocations += 1
locationsVisited.append(posStr)

for char in lines:
    if char == "^":
        yPos += 1
    if char == "v":
        yPos -= 1
    if char == "<":
        xPos -= 1
    if char == ">":
        xPos += 1

    posStr = str(xPos)+":"+str(yPos)
    if posStr not in locationsVisited:
        countDifferentLocations += 1
        locationsVisited.append(posStr)

    

print(countDifferentLocations)