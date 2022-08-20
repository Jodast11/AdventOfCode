import math
import time
import threading

def doStep(z,div1,add1,add2,inp):
    x = int(((z%26)+add1) != inp)
    y = 26 if x else 1
    z = math.floor(z/div1)*y
    y = inp+add2 if x else 0
    return z+y

def getValidZValues(prevValid,startZ,blockSize,div1,add1,add2, results):
    for z in range(startZ,startZ+blockSize):
        for inp in range(1,10):
            zValue = doStep(z,div1,add1,add2,inp)
            if zValue in prevValid:
                results.append(z)

input = open("input.txt").read().split("inp w\n")[1:]

div1 = []
add1 = []
add2 = []

for line in input:
    instructions = line.split("\n")
    div1.append(int(instructions[3].split(" ")[-1]))
    add1.append(int(instructions[4].split(" ")[-1]))
    add2.append(int(instructions[14].split(" ")[-1]))

alowedZValues = [[0]]

threadCount = 20

for i in range(14):
    startTime = time.time()
    threads = []
    threadResults = []
    for threadId in range(20):
        threadResults.append([])
        threads.append(threading.Thread(target=getValidZValues, args=(alowedZValues[i],int(1000000/threadCount)*threadId,int(1000000/threadCount),div1[-i-1],add1[-i-1],add2[-i-1],threadResults[threadId])))
        threads[threadId].start()
    for thread in threads:
        thread.join()
    # print(threadResults)
    
    newAllowedZValues = []
    for threadResult in threadResults:
        for value in threadResult:
            newAllowedZValues.append(value)

    alowedZValues.append(newAllowedZValues)

    print(time.time()-startTime)

    # newAllowedZValues = []
    # for z in range(1000000):
    #     for inp in range(1,10):
    #         zValue = doStep(z,div1[-i-1],add1[-i-1],add2[-i-1],inp)
    #         if zValue in alowedZValues[i] and z not in newAllowedZValues:
    #             newAllowedZValues.append(z)
    # alowedZValues.append(newAllowedZValues)

# alowedZValues = alowedZValues[::-1]
print(alowedZValues)