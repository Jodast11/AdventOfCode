def flash(energyLevels,y,x,alreadyFlashed):
    alreadyFlashed.append((x,y))
    for yOffset in range(-1,2):
        for xOffset in range(-1,2):
            if x+xOffset >= 0 and y+yOffset >= 0 and x+xOffset < len(energyLevels) and y+yOffset < len(energyLevels):
                if (x+xOffset,y+yOffset) not in alreadyFlashed:
                    energyLevels[y+yOffset][x+xOffset] += 1
                    if energyLevels[y+yOffset][x+xOffset] > 9:
                        energyLevels, alreadyFlashed = flash(energyLevels,y+yOffset,x+xOffset,alreadyFlashed)
    return energyLevels, alreadyFlashed

inputRaw = [line.strip() for line in open("input.txt")]

energyLevels = []
alreadyFlashed = []
totalFlashes = 0

for line in inputRaw:
    newLine = []
    for energyLevel in line:
        newLine.append(int(energyLevel))
    energyLevels.append(newLine)

for i in range(100):
    for y, line in enumerate(energyLevels):
        for x, energyLevel in enumerate(line):
            energyLevels[y][x] += 1

    for y, line in enumerate(energyLevels):
        for x, energyLevel in enumerate(line):
            if energyLevels[y][x] > 9:
                if (x,y) not in alreadyFlashed:
                    energyLevels, alreadyFlashed = flash(energyLevels,y,x,alreadyFlashed)

    totalFlashes += len(alreadyFlashed)
    for x,y in alreadyFlashed:
        energyLevels[y][x] = 0
    alreadyFlashed = []



print(totalFlashes)