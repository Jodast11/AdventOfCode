lines = [int(y) for y in [x.strip() for x in open("input.txt")][0].split(",")]

calculatedFuels = []

for distance in range(max(lines)+1):
    fuelTotal = 0
    for line in lines:
        fuelTotal += abs(distance-line)
    calculatedFuels.append(fuelTotal)

print(min(calculatedFuels))