from dis import Instruction
import os

with open(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt", "r") as f:
    compressedData = f.read().split("\n")[0]

uncompressedData = ""

currentPosition = 0

while currentPosition < len(compressedData):
    if compressedData[currentPosition] == "(":
        instructionRaw = compressedData[currentPosition+1:compressedData.find(")",currentPosition)]
        repeat = int(instructionRaw.split("x")[1])
        dataLength = int(instructionRaw.split("x")[0])
        for i in range(repeat):
            uncompressedData += compressedData[currentPosition+len(instructionRaw)+2:currentPosition+len(instructionRaw)+2+dataLength]
        currentPosition += len(instructionRaw)+dataLength+2
    else:
        uncompressedData += compressedData[currentPosition]
        currentPosition += 1

print(uncompressedData)
print(len(uncompressedData))