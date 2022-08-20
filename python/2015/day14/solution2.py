lines = [x.strip() for x in open("input.txt")]

def findDistanceTraveled(speed, powerTime, restTime, time):
    distanceTraveled = 0
    cycleTime = powerTime + restTime
    wholeCyclesCompleted = time // cycleTime
    timeLeft = time - (wholeCyclesCompleted*cycleTime)
    distanceTraveled += wholeCyclesCompleted*speed*powerTime
    if timeLeft >= powerTime:
        distanceTraveled += speed*powerTime
    else:
        distanceTraveled += timeLeft*speed
    return distanceTraveled

    
reindeerScores = [0 for i in range(9)]

for i in range(1,2504):
    reindeerDistances = []

    for line in lines:
        parts = line.split(" ")  
        reindeerDistances.append(findDistanceTraveled(int(parts[3]),int(parts[6]),int(parts[-2]),i))
    
    highestDistance = max(reindeerDistances)
    for reindeerId, reindeerDistance in enumerate(reindeerDistances):
        if reindeerDistance == highestDistance:
            reindeerScores[reindeerId] += 1

# findDistanceTraveled(16,11,162,1000)
# print(max(reindeerScores))
print(max(reindeerScores))