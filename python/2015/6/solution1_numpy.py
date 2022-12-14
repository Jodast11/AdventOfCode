import numpy as np
import time

startTime = time.time()

instructions = [x.strip().replace("turn ","").replace(","," ") for x in open("input.txt")]

leds = np.zeros((1000, 1000))

def applyOperation(operation, xStart, yStart, xEnd, yEnd):
    operation = int(operation.replace("on","1").replace("off","0").replace("toggle","2"))
    if operation < 2:
        for x in range(xStart, xEnd+1):
            for y in range(yStart, yEnd+1):
                leds[x][y] = operation
    else:
        for x in range(xStart, xEnd+1):
            for y in range(yStart, yEnd+1):
                leds[x][y] = 0 if leds[x][y] else 1
            

for instruction in instructions:
    operation, xStart, yStart, _, xEnd, yEnd = instruction.split(" ")
    applyOperation(operation, int(xStart), int(yStart), int(xEnd), int(yEnd))

print(leds.sum())

print(time.time()-startTime)
