lines = [int(y) for y in [x.strip() for x in open("input.txt")][0].split(",")]

def calculateFuel(distance):
    return int((distance*(distance+1))/2)

calculatedFuels = []

for distance in range(max(lines)+1):
    fuelTotal = 0
    for line in lines:
        fuelTotal += calculateFuel(abs(distance-line))
    calculatedFuels.append(fuelTotal)

print(min(calculatedFuels))
# print(calculateFuel(11))