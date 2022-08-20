with open("input.txt") as f:
    input = f.readlines()

locationsVisited = []
countDifferentLocations = 0

xPos = 0
yPos = 0
posStr = str(xPos)+str(yPos)
countDifferentLocations += 1
locationsVisited.append(posStr)

for char in input[0]:
    if char == "^":
        yPos += 1
    if char == "v":
        yPos -= 1
    if char == "<":
        xPos -= 1
    if char == ">":
        xPos += 1

    posStr = str(xPos)+str(yPos)
    print(posStr+char)
    if posStr not in locationsVisited:
        countDifferentLocations += 1
        locationsVisited.append(posStr)

    

print(countDifferentLocations)