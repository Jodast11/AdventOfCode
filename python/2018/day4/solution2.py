import os
import time

startTime = time.time()

with open(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt", "r") as f:
    lines = f.read().split("\n")

lines.sort()

currentGuardId = -1
sleepingSince = 0

sleepShedules = {}

def parseTime(line):
    parts = [int(x) for x in line.split(" ")[1][:-1].split(":")]
    return parts[1]

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

def order(nr):
    return nr[1]

topMinutes = []

for guardId in sleepShedules:
    maxMinute = -1
    count = 0
    for i in range(60):
        if sleepShedules[guardId].count(i) > count:
            maxMinute = i
            count = sleepShedules[guardId].count(i)
    
    topMinutes.append((maxMinute, count, guardId))

topMinutes.sort(key=order)

print(f"{topMinutes[-1][0] * topMinutes[-1][2]}:{time.time()-startTime}")