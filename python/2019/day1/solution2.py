import math

input = [int(line.strip()) for line in open("input.txt").readlines()]

def calculateRequiredFuel(mass):
    requiredFuel = math.floor(mass/3) - 2
    if requiredFuel <= 0:
        return 0
    else:
        return requiredFuel + calculateRequiredFuel(requiredFuel)

print(sum([calculateRequiredFuel(mass) for mass in input]))