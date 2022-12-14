import os
import time

with open(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt", "r") as f:
    compressedData = f.read().split("\n")[0]

def getDecompressedLength(compressedData):
    uncompressedDataLength = 0
    currentPosition = 0
    while currentPosition < len(compressedData):
        if compressedData[currentPosition] == "(":
            instructionRaw = compressedData[currentPosition+1:compressedData.find(")",currentPosition)]
            repeat = int(instructionRaw.split("x")[1])
            dataLength = int(instructionRaw.split("x")[0])
            uncompressedDataLength += getDecompressedLength(compressedData[currentPosition+len(instructionRaw)+2:currentPosition+len(instructionRaw)+2+dataLength])*repeat
            currentPosition += len(instructionRaw)+dataLength+2
        else:
            uncompressedDataLength += 1
            currentPosition += 1
    
    return uncompressedDataLength

print(getDecompressedLength(compressedData))