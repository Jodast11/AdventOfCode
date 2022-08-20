from itertools import combinations
import itertools

def getValue(programm, value, mode):
    return value if mode else programm[value]

def getMode(modes, index):
    return modes[index] if index < len(modes) else 0

def runProgramm(programmInput, input, index):
    programm = [i for i in programmInput]

    currentIndex = index

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
            programm[programm[currentIndex+1]] = input.pop(0)
            instructionLength = 2
        elif instruction == 4: #return True (programm running), index, output value, programm, input
            return (True, currentIndex + 2, getValue(programm, programm[currentIndex + 1], getMode(modes, 0)), programm, input)
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
            return [False]
        else:
            print("Error")
            break
        
        currentIndex += instructionLength

def testSequence(programmInput, sequence):
    inputs = [[nr] for nr in sequence]
    programms = [[i for i in programmInput] for j in range(5)]
    indexes = [0 for i in range(5)]
    programmRunning = [True for i in range(5)]
    inputs[0].append(0)
    while False not in programmRunning:
        for i in range(5):
            output = runProgramm(programms[i], inputs[i], indexes[i])
            programmRunning[i] = output[0]
            if output[0]:
                indexes[i] = output[1]
                inputs[(i+1)%5].append(output[2])
                programms[i] = output[3]
                inputs[i] = output[4]
    return inputs[0][0]

def getBestSequnce(programmInput):
    print(max([testSequence(programmInput, sequnce) for sequnce in list(itertools.permutations(range(5,10)))]))

programm = [int(x) for x in [line.strip() for line in open("input.txt").readlines()][0].split(",")]

getBestSequnce(programm)