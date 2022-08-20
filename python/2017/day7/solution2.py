class Programm:
    def __init__(self, thisProgramName, aboveProgramms=None, programmWeight=None):
        self.thisProgramName = thisProgramName
        self.aboveProgramms = aboveProgramms
        self.lowerProgramm = None
        self.programmWeight = programmWeight

    def __repr__(self) -> str:
        return f"{self.lowerProgramm}->{self.thisProgramName}({str(self.programmWeight)})->{self.aboveProgramms}"

allInformation = [information.strip() for information in open("input.txt","r").readlines()]

programms = {}

for information in allInformation:
    parts = information.split(" -> ")
    thisProgramm = parts[0].split(" ")[0]
    programmWeight = int(parts[0].split(" ")[1].replace("(","").replace(")",""))
    subPrograms = parts[1].replace(" ","").split(",") if len(parts) > 1 else []

    if thisProgramm in programms:
        programms[thisProgramm].aboveProgramms = subPrograms
        programms[thisProgramm].programmWeight = programmWeight
    else:
        programms[thisProgramm] = Programm(thisProgramm, subPrograms, programmWeight)

    for subProgramm in subPrograms:
        if subProgramm not in programms:
            programms[subProgramm] = Programm(subProgramm)
        programms[subProgramm].lowerProgramm = thisProgramm

def getTowerWeight(programmName):
    totalWeight = programms[programmName].programmWeight
    for subProgramm in programms[programmName].aboveProgramms:
        totalWeight += getTowerWeight(subProgramm)
    return totalWeight

def getUnbalanced(programmName):
    subProgrammNames = [subProgrammName for subProgrammName in programms[programmName].aboveProgramms]
    subProgrammWeights = [getTowerWeight(subProgrammName) for subProgrammName in subProgrammNames]
    if len(set(subProgrammWeights)) > 1:
        for i, value in enumerate(subProgrammWeights):
            if subProgrammWeights.count(value) == 1:
                print(subProgrammNames[subProgrammWeights.index(value)])
                print(programms[subProgrammNames[subProgrammWeights.index(value)]].programmWeight-(value-subProgrammWeights[(i+1)%(len(subProgrammNames))]))
        exit()
    for subProgrammName in programms[programmName].aboveProgramms:
        getUnbalanced(subProgrammName)

for programmName in programms:
    if not programms[programmName].lowerProgramm:
        bottomProgramm = programmName

getUnbalanced(bottomProgramm)