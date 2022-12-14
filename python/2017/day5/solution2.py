instructions = [int(line.strip()) for line in open("input.txt","r")]

currentPos = 0
stepCounter = 0

while currentPos < len(instructions) and currentPos >= 0:
    if instructions[currentPos] >= 3:
        instructions[currentPos] -= 1
        currentPos += instructions[currentPos] + 1
    else:
        instructions[currentPos] += 1
        currentPos += instructions[currentPos] - 1
    stepCounter += 1

print(stepCounter)