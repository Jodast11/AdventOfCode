import math

input = [int(line.strip()) for line in open("input.txt").readlines()]

def calculateRequiredFuel(mass):
    return math.floor(mass/3) - 2

print(sum([calculateRequiredFuel(mass) for mass in input]))