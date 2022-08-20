import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Input.txt')
lines = [x.strip() for x in open(filename)]

def isValid(value, rawRules):
    for ruleSet in rawRules:
        for numSet in ruleSet:
            if value >= numSet[0] and value <= numSet[1]:
                return False
    return True
    

def getRules():
    rules = {}
    for line in lines:
        if len(line) == 0:
            break
        
        key, value = line.split(": ")[0], [[int(z) for z in x.split("-")] for x in line.split(": ")[1].split(" or ")]
        rules[key] = value
    
    return [rules[x] for x in rules], rules

def findValidTickets(rules):
    invalidIndexe = []
    otherTickets = [[int(x) for x in lines[ticketIndex].split(",")] for ticketIndex in range(lines.index("nearby tickets:") + 1, len(lines))]
    for otherTicketIndex in range(len(otherTickets)):
        for value in otherTickets[otherTicketIndex]:
            if isValid(value, rules) and otherTicketIndex not in invalidIndexe:
                invalidIndexe.append(otherTicketIndex) 
            elif otherTicketIndex in invalidIndexe:
                continue

    realTickets = []
    for ticketIndex in range(len(otherTickets)):
        if ticketIndex not in invalidIndexe:
            realTickets.append(otherTickets[ticketIndex])

    return realTickets

def getListOfInvalidIds(value, dicRules):
    invalid = []
    for ruleId in dicRules.keys():
        if isValid(value, [dicRules[ruleId]]) and ruleId not in invalid:
            invalid.append(ruleId)
        elif ruleId in invalid:
            continue

    return invalid

def getCleanedIds(oldIds, counter):
    newIds = oldIds.copy()
    for value in newIds:
        if len(newIds[value]) == 1:
            for key in newIds:
                if key != value and newIds[value][0] in newIds[key]:
                    newIds[key].remove(newIds[value][0])
    
    if counter != len(oldIds):
        counter += 1
        return getCleanedIds(newIds, counter)
    else:
        return newIds


def determineField():
    rulesRaw, rules = getRules()
    keys = list(rules.keys())
    realTickets = findValidTickets(rulesRaw)
    positionIds = {i:keys.copy() for i in range(len(rules))}
    for realTicket in realTickets:
        for numIndex, number in enumerate(realTicket):
            invalidList = getListOfInvalidIds(number, rules)
            for invalid in invalidList:
                if invalid in keys:
                    positionIds[numIndex].remove(invalid)
    return positionIds

    

posIds = determineField()
realSolution = getCleanedIds(posIds, 0)
sol = 1
myTicket = [137,173,167,139,73,67,61,179,103,113,163,71,97,101,109,59,131,127,107,53]
for key in realSolution:
    if "departure" in realSolution[key][0].split(" ")[0]:
        sol *= myTicket[key]