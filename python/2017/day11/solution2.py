directions = [direction for direction in open("input.txt","r").readlines()[0].strip().split(",")]

totalVertical = 0
totalHorizontal = 0

posVeritcal = ["ne", "n", "nw"]
negVeritcal = ["se", "s", "sw"]

posHorizontal = ["ne","se"]
negHorizontal = ["nw","sw"]

allDistances = []

for direction in directions:
    if direction in posVeritcal:
        totalVertical += 1
    if direction in negVeritcal:
        totalVertical -= 1
    if direction in posHorizontal:
        totalHorizontal += 1
    if direction in negHorizontal:
        totalHorizontal -= 1
    allDistances.append(max([abs(totalHorizontal), abs(totalVertical)]))

print(max(allDistances))