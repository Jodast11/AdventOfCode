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
    

reindeerDistance = []

for line in lines:
    parts = line.split(" ")  
    reindeerDistance.append(findDistanceTraveled(int(parts[3]),int(parts[6]),int(parts[-2]),2503))

# findDistanceTraveled(16,11,162,1000)
print(max(reindeerDistance))