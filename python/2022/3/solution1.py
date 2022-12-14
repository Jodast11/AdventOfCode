import string

rucksacks = [x.strip() for x in open("input.txt").readlines()]

def getPriority(element):
    allCharacters = string.ascii_lowercase + string.ascii_uppercase
    return allCharacters.index(element) + 1

def getDuplicate(arrA, arrB):
    result = []
    for element in arrA:
        if element in arrB:
            result.append(element)
    return result

result = 0

for rucksack in rucksacks:
    compartMentSize = int(len(rucksack)/2)
    compartmentA, compartmentB = list(set(rucksack[:compartMentSize])), list(set(rucksack[compartMentSize:]))
    result += getPriority(getDuplicate(compartmentA, compartmentB)[0])

print(result)