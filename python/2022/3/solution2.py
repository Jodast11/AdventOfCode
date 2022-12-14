import string
import re

rawInput = open("input.txt").read()

groups = [group[:-1].split("\n") for group in re.findall(".+\\n.+\\n.+\\n", rawInput)]

def getPriority(element):
    allCharacters = string.ascii_lowercase + string.ascii_uppercase
    return allCharacters.index(element) + 1

def intersects(rucksacks):
    result = set(rucksacks[0])
    for rucksack in rucksacks[1:]:
        result = result.intersection(set(rucksack))
    return list(result)[0]

print(sum([getPriority(intersects(group)) for group in groups]))