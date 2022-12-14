import string
import os

def ignoreLetter(polymer, letter):
    output = ""
    for x in polymer:
        if x != letter and x != letter.upper():
            output += x
    return output

def fullyReact(inputPolymer):
    reactants = [string.ascii_lowercase[i] + string.ascii_uppercase[i] for i in range(len(string.ascii_lowercase))]

    prevLength = len(inputPolymer) + 1

    while len(inputPolymer) < prevLength:
        prevLength = len(inputPolymer)
        for reactant in reactants:
            inputPolymer = inputPolymer.replace(reactant, "")
            inputPolymer = inputPolymer.replace(reactant[::-1], "")

    return inputPolymer

with open(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt", "r") as f:
    inputPolymer = f.read().split("\n")[0]

print(min([len(fullyReact(ignoreLetter(inputPolymer, letterToRemove))) for letterToRemove in string.ascii_lowercase]))