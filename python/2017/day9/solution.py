import json

characterStream = [instruction.strip() for instruction in open("input.txt","r").readlines()][0]

openedGroups = 0
closedGroups = 0

inGarbage = False
ignoreNext = False

score = 0
garbageCount = 0

for i, character in enumerate(characterStream):
    if not ignoreNext:
        if not inGarbage:
            if character == "{":
                openedGroups += 1
            elif character == "}":
                score += openedGroups-closedGroups
                closedGroups += 1
            elif character == "<":
                inGarbage = True
        else:
            if character == "!":
                ignoreNext = True
            elif character == ">":
                inGarbage = False
            else:
                garbageCount += 1
    else:
        ignoreNext = False    

print(f"Solution 1: {score}")
print(f"Solution 2: {garbageCount}")