import math
import json

def checkRequiredOpperation(number): #0:None, 1:explode, 2: split
    numbers = "0123456789"
    nestDepth = 0
    twoDigits = False
    for index, simbol in enumerate(number):
        if simbol == "[":
            nestDepth += 1
            if nestDepth == 5:
                return 1
        if simbol == "]":
            nestDepth -= 1
        if simbol in numbers:
            if number[index+1] in numbers:
                twoDigits = True
    if not twoDigits:
        return 0
    return 2

def explode(number):
    numbers = "0123456789"
    #find the pair
    nestDepth = 0
    for pairStartIndex, simbol in enumerate(number):
        if simbol == "[": nestDepth += 1
        if simbol == "]": nestDepth -= 1
        if nestDepth == 5: break
    pairEndIndex = number[pairStartIndex:].find("]")+pairStartIndex
    pair = [int(i) for i in number[pairStartIndex+1:pairEndIndex].split(",")]
    
    #find the first regular number to the left of the pair
    leftNumberString = ""
    leftNumberStartIndex = 0
    for i in range(pairStartIndex,-1,-1):
        if number[i] in numbers:
            leftNumberStartIndex = i
            leftNumberString += number[i]
            for j in range(i-1,-1,-1):
                if number[j] in numbers:
                    leftNumberString += number[j]
                    leftNumberStartIndex -= 1
                else:
                    break
            break
    if len(leftNumberString):
        leftNumber = int(leftNumberString[::-1])
    else:
        leftNumber = None

    #find the first regular number to  the right
    rightNumberString = ""
    rightNumberStartIndex = 0
    for i in range(pairEndIndex,len(number)):
        if number[i] in numbers:
            rightNumberStartIndex = i
            rightNumberString += number[i]
            for j in range(i+1,len(number)):
                if number[j] in numbers:
                    rightNumberString += number[j]
                else:
                    break
            break
    if len(rightNumberString):
        rightNumber = int(rightNumberString)
    else:
        rightNumber = None

    # rebuild new number
    newNumber = ""
    if leftNumber == None:
        newNumber += number[:pairStartIndex]
    else:
        newNumber += number[:leftNumberStartIndex]
        newNumber += str(leftNumber + pair[0])
        newNumber += number[leftNumberStartIndex+len(leftNumberString):pairStartIndex]
    
    newNumber += "0"

    if rightNumber == None:
        newNumber += number[pairEndIndex+1:]
    else:
        newNumber += number[pairEndIndex+1:rightNumberStartIndex]
        newNumber += str(pair[1]+rightNumber)
        newNumber += number[rightNumberStartIndex+len(rightNumberString):]


    return newNumber

def split(number):
    numbers = "0123456789"
    numberString = ""
    numberStartIndex = 0
    numberEndIndex = 0
    for i in range(len(number)):
        if number[i] in numbers:
            numberStartIndex = i
            numberString += number[i]
            for j in range(i+1,len(number)):
                if number[j] in numbers:
                    numberString += number[j]
                else:
                    break
            if len(numberString) > 1:
                break
            else:
                numberString = ""
    numberEndIndex = numberStartIndex + len(numberString)
    numberToSplit = int(numberString)

    newNumberString = ""
    newNumberString += number[:numberStartIndex]
    newNumberString += "["
    newNumberString += str(math.floor(numberToSplit/2))
    newNumberString += ","
    newNumberString += str(math.ceil(numberToSplit/2))
    newNumberString += "]"
    newNumberString += number[numberEndIndex:]
    return newNumberString
                
def reduce(number):
    requiredOpperation = checkRequiredOpperation(number)

    while requiredOpperation != 0:
        if requiredOpperation == 1:
            number = explode(number)
        else:
            number = split(number)
        requiredOpperation = checkRequiredOpperation(number)
    return number

def add(number1,number2):
    return "["+number1+","+number2+"]"

def calculateMagnetude(numberRaw):
    number = json.loads(numberRaw)
    if type(number) == int:
        return number
    numberPartOne = number[0]
    numberPartTwo = number[1]
    return calculateMagnetude(json.dumps(numberPartOne)) * 3 + calculateMagnetude(json.dumps(numberPartTwo)) * 2
    
    


lines = [line.strip() for line in open("input.txt").readlines()]

number = lines[0]

for line in lines[1:]:
    number = add(number,line)
    number = reduce(number)

allMagnetudes = []

for numberOne in lines:
    for numberTwo in lines:
        if numberOne != numberTwo:
            number = add(numberOne,numberTwo)
            number = reduce(number)
            allMagnetudes.append(calculateMagnetude(number))

print(max(allMagnetudes))