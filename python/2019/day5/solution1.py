def getValue(programm, value, mode):
    return value if mode else programm[value]

def getMode(modes, index):
    return modes[index] if index < len(modes) else 0

def runProgramm(programmInput, input):
    programm = [i for i in programmInput]

    currentIndex = 0

    while True:
        instructionString = str(programm[currentIndex])
        instruction = int(str(instructionString)[-2:])
        modes = [int(x) for x in instructionString[:-2][::-1]]
        if instruction == 1:
            programm[programm[currentIndex+3]] = getValue(programm, programm[currentIndex + 1], getMode(modes, 0)) + getValue(programm, programm[currentIndex + 2], getMode(modes, 1))
            instructionLength = 4
        elif instruction == 2:
            programm[programm[currentIndex+3]] = getValue(programm, programm[currentIndex + 1], getMode(modes, 0)) * getValue(programm, programm[currentIndex + 2], getMode(modes, 1))
            instructionLength = 4
        elif instruction == 3:
            programm[programm[currentIndex+1]] = input
            instructionLength = 2
        elif instruction == 4:
            print(getValue(programm, programm[currentIndex + 1], getMode(modes, 0)))
            instructionLength = 2
        elif instruction == 99:
            break
        else:
            print("Error")
            break

        currentIndex += instructionLength


programm = [int(x) for x in [line.strip() for line in open("input.txt").readlines()][0].split(",")]

runProgramm(programm, 1)