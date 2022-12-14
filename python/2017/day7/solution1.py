class Programm:
    def __init__(self, thisProgramName, aboveProgramms=None):
        self.thisProgramName = thisProgramName
        self.aboveProgramms = aboveProgramms
        self.lowerProgramm = None

    def __repr__(self) -> str:
        return f"{self.lowerProgramm}->{self.thisProgramName}->{self.aboveProgramms}"

allInformation = [information.strip() for information in open("input.txt","r").readlines()]

programms = {}

for information in allInformation:
    parts = information.split("->")
    thisProgramm = parts[0].split(" ")[0]
    subPrograms = parts[1].replace(" ","").split(",") if len(parts) > 1 else []

    if thisProgramm in programms:
        programms[thisProgramm].aboveProgramms = subPrograms
    else:
        programms[thisProgramm] = Programm(thisProgramm, subPrograms)

    for subProgramm in subPrograms:
        if subProgramm not in programms:
            programms[subProgramm] = Programm(subProgramm)
        programms[subProgramm].lowerProgramm = thisProgramm

for programmName in programms:
    if not programms[programmName].lowerProgramm:
        print(programmName)

#print(programms)