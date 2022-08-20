def createRanges(rangesRaw):
    rangesRaw = rangesRaw.split(" or ")
    ranges = []
    for rangeRaw in rangesRaw:
        ranges.append([int(rangeRaw.split("-")[0]),int(rangeRaw.split("-")[-1])])
    return ranges

def isFieldValid(fieldValue, possibleRanges):
    for possibleRange in possibleRanges:
        if fieldValue >= possibleRange[0] and fieldValue <= possibleRange[-1]:
            return True
    return False

inputRaw = open("Input.txt").read().split("\n\n")

rulesRaw = inputRaw[0].split("\n")

nearbyTickets = [[int(field) for field in ticket.split(",")] for ticket in inputRaw[2].split("\n")[1:]]

rules = {rule.split(": ")[0]:createRanges(rule.split(": ")[1]) for rule in rulesRaw}

allRules = []

for fieldType in rules:
    for possibeRange in rules[fieldType]:
        allRules.append(possibeRange)

errorRate = 0

for nearbyTicket in nearbyTickets:
    for value in nearbyTicket:
        if not isFieldValid(value, allRules):
            errorRate += value

print(errorRate)