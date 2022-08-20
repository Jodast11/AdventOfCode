with open("input.txt") as f:
    linesCleaned = [int(x.strip()) for x in f.readlines()]

timesIncreased = 0
lastDepth = 99999
for depth in linesCleaned:
    if depth > lastDepth:
        timesIncreased += 1
    lastDepth = depth

print(timesIncreased)