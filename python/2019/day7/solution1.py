from itertools import combinations
import itertools

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
            programm[programm[currentIndex+1]] = input.pop()
            instructionLength = 2
        elif instruction == 4:
            return getValue(programm, programm[currentIndex + 1], getMode(modes, 0))
        elif instruction == 5:
            if getValue(programm, programm[currentIndex + 1], getMode(modes, 0)) != 0:
                currentIndex = getValue(programm, programm[currentIndex + 2], getMode(modes, 1))
                instructionLength = 0
            else:
                instructionLength = 3
        elif instruction == 6:
            if getValue(programm, programm[currentIndex + 1], getMode(modes, 0)) == 0:
                currentIndex = getValue(programm, programm[currentIndex + 2], getMode(modes, 1))
                instructionLength = 0
            else:
                instructionLength = 3
        elif instruction == 7:
            programm[programm[currentIndex+3]] = int(getValue(programm, programm[currentIndex + 1], getMode(modes, 0)) < getValue(programm, programm[currentIndex + 2], getMode(modes, 1)))
            instructionLength = 4
        elif instruction == 8:
            programm[programm[currentIndex+3]] = int(getValue(programm, programm[currentIndex + 1], getMode(modes, 0)) == getValue(programm, programm[currentIndex + 2], getMode(modes, 1)))
            instructionLength = 4
        elif instruction == 99:
            break
        else:
            print("Error")
            break
        
        currentIndex += instructionLength

def testSequence(programmInput, sequence):
    output = 0
    for i in range(5):
        output = runProgramm(programmInput, [output, sequence[i]])
    return output

def getBestSequnce(programmInput):
    print(max([testSequence(programmInput, sequnce) for sequnce in list(itertools.permutations(range(5)))]))
        



programm = [int(x) for x in [line.strip() for line in open("input.txt").readlines()][0].split(",")]

getBestSequnce(programm)