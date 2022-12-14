import os
import copy

with open(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt", "r") as f:
    lines = f.read().split("\n")

lines.sort()

currentGuardId = -1
sleepingSince = 0

sleepShedules = {}

def parseTime(line):
    parts = [int(x) for x in line.split(" ")[1][:-1].split(":")]
    return parts[1]

def getIndex(nr):
    return sleepShedules[maxId].count(nr)

for line in lines:
    if "#" in line:
        idStartPos = line.index("#")+1
        currentGuardId = int(line[idStartPos:line.index(" ", idStartPos)])
    elif "asleep" in line:
        sleepingSince = parseTime(line)
    elif "wakes" in line:
        if currentGuardId in sleepShedules:
            for i in range(sleepingSince, parseTime(line)):
                sleepShedules[currentGuardId].append(i)
        else:
            sleepShedules[currentGuardId] = [i for i in range(sleepingSince, parseTime(line))]

maxMins = 0
maxId = -1

for guardId in sleepShedules:
    if len(sleepShedules[guardId]) > maxMins:
        maxMins = len(sleepShedules[guardId])
        maxId = guardId

maxGuardSleepScedule = copy.deepcopy(sleepShedules[maxId])

maxGuardSleepScedule.sort(key=getIndex)

print(maxGuardSleepScedule[-1] * maxId)