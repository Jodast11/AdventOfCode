from curses.ascii import isascii


def getValue(programm, value, mode, relativeBase, isAddress):
    if not isAddress:
        if mode == 1:
            return value

        index = value if mode == 0 else relativeBase+value

        if index in programm.keys():
            return programm[index]
        else:
            return 0
    else:
        if mode == 0 or mode == 1:
            return value
        else:
            return relativeBase + value

def getMode(modes, index):
    return modes[index] if index < len(modes) else 0

def runProgramm(programm, inputs):
    currentIndex = 0

    relativeBase = 0

    while True:
        instructionString = str(programm[currentIndex])
        instruction = int(str(instructionString)[-2:])
        modes = [int(x) for x in instructionString[:-2][::-1]]

        if instruction == 1: #Add
            programm[getValue(programm, programm[currentIndex + 3], getMode(modes, 2), relativeBase, True)] = getValue(programm, programm[currentIndex + 1], getMode(modes, 0), relativeBase, False) + getValue(programm, programm[currentIndex + 2], getMode(modes, 1), relativeBase, False)
            instructionLength = 4
        elif instruction == 2: #Subtract
            programm[getValue(programm, programm[currentIndex + 3], getMode(modes, 2), relativeBase, True)] = getValue(programm, programm[currentIndex + 1], getMode(modes, 0), relativeBase, False) * getValue(programm, programm[currentIndex + 2], getMode(modes, 1), relativeBase, False)
            instructionLength = 4
        elif instruction == 3: #Get input
            programm[getValue(programm, programm[currentIndex + 1], getMode(modes, 0), relativeBase, True)] = inputs
            instructionLength = 2
        elif instruction == 4: #Output
            print(getValue(programm, programm[currentIndex + 1], getMode(modes, 0), relativeBase, False))
            instructionLength = 2
        elif instruction == 5:
            if getValue(programm, programm[currentIndex + 1], getMode(modes, 0), relativeBase, False) != 0:
                currentIndex = getValue(programm, programm[currentIndex + 2], getMode(modes, 1), relativeBase, False)
                instructionLength = 0
            else:
                instructionLength = 3
        elif instruction == 6:
            if getValue(programm, programm[currentIndex + 1], getMode(modes, 0), relativeBase, False) == 0:
                currentIndex = getValue(programm, programm[currentIndex + 2], getMode(modes, 1), relativeBase, False)
                instructionLength = 0
            else:
                instructionLength = 3
        elif instruction == 7:
            programm[getValue(programm, programm[currentIndex + 3], getMode(modes, 2), relativeBase, True)] = int(getValue(programm, programm[currentIndex + 1], getMode(modes, 0), relativeBase, False) < getValue(programm, programm[currentIndex + 2], getMode(modes, 1), relativeBase, False))
            instructionLength = 4
        elif instruction == 8:
            programm[getValue(programm, programm[currentIndex + 3], getMode(modes, 2), relativeBase, True)] = int(getValue(programm, programm[currentIndex + 1], getMode(modes, 0), relativeBase, False) == getValue(programm, programm[currentIndex + 2], getMode(modes, 1), relativeBase, False))
            instructionLength = 4
        elif instruction == 9:
            relativeBase += getValue(programm, programm[currentIndex + 1], getMode(modes, 0), relativeBase, False)
            instructionLength = 2
        elif instruction == 99: #Programm finished
            break
        else:
            print("Error")
            break
        
        currentIndex += instructionLength

programmList = [int(x) for x in [line.strip() for line in open("input.txt").readlines()][0].split(",")]

programm = {}

for index, value in enumerate(programmList):
    programm[index] = value

runProgramm(programm, 1)