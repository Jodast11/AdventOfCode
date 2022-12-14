import string
import os

with open(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt", "r") as f:
    inputPolymer = f.read().split("\n")[0]

reactants = [string.ascii_lowercase[i] + string.ascii_uppercase[i] for i in range(len(string.ascii_lowercase))]

prevLength = len(inputPolymer) + 1

while len(inputPolymer) < prevLength:
    prevLength = len(inputPolymer)
    for reactant in reactants:
        inputPolymer = inputPolymer.replace(reactant, "")
        inputPolymer = inputPolymer.replace(reactant[::-1], "")

print(len(inputPolymer))