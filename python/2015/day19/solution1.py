import re

class Opperation:
    def __init__(self, toReplace, replaceWith) -> None:
        self.toReplace = toReplace
        self.replaceWith = replaceWith
    
    def getAllOperationResults(self, molekule):
        resultingMolekules = []
        for toReplaceIndex in [m.start() for m in re.finditer(self.toReplace, molekule)]:
            resultingMolekules.append(molekule[:toReplaceIndex]+self.replaceWith+molekule[toReplaceIndex+len(self.toReplace):])
        return resultingMolekules

input = [x.strip() for x in open("input.txt")]

startingMolekule = input[-1]
rawReplacementPosibilities = input[:-2]

possibleOperations = []

for rawReplacementPosibilitie in rawReplacementPosibilities:
    target, destination = rawReplacementPosibilitie.split(" => ")
    possibleOperations.append(Opperation(target, destination))

resultingMolekules = []

for operation in possibleOperations:
    for resultingMolekule in operation.getAllOperationResults(startingMolekule):
        resultingMolekules.append(resultingMolekule)

print(len(list(set(resultingMolekules))))