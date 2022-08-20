from cgitb import reset
import json
import math

lines = [line.strip() for line in open("input.txt").readlines()]  

def getExplodable(number, currentDepth=0):
    if type(number) == int:
        return [False, []]
    if currentDepth == 4:
        return [True, []]
    for index, element in enumerate(number):
        [explodable, path] = getExplodable(element, currentDepth+1)
        if explodable:
            return [True, [index]+path]
    return [False, []]

def getSplitable(number):
    if type(number) == int:
        if number>9: return [True, []]
        return [False, []]
    for index, element in enumerate(number):
        if type(element) == int:
            if element > 9:
                return [True, [index]]
        [splitable, path] = getSplitable(element)
        if splitable:
            return [True, [index]+path]
    return [False, []]

def getRequiedOperation(number): #0:none 1:explode 2:split | path
    [explodable, path] = getExplodable(number)
    if explodable:
        return [1, path]

    [splitable, path] = getSplitable(number)
    if splitable:
        return [2, path]

    return [0, []]

def getNumber(number, path):
    if len(path) == 0:
        return number
    return getNumber(number[path[0]], path[1:])

def replace(number, path, replacement):
    result = []
    if len(path) == 0: return replacement
    if type(number) == int:
        return number
    for index, element in enumerate(number):
        if index == path[0]:
            result.append(replace(element, path[1:], replacement))
        else:
            result.append(element)
    return result

def getNextRegularNumber(number, pathOrig, inverted):
    path = pathOrig[:]
    try:
        path[-1] += 1 - (inverted * 2)

        while 2 in path or -1 in path:
            path[-2] += 1 - (inverted * 2)
            path = path[:-1]

        while type(getNumber(number, path)) != int:
            path += [int(inverted)]

        return path

    except:
        return []

def explode(number, path):
    parts = getNumber(number, path)
    leftNumber = parts[0]
    rightNumber = parts[1]
    rightPath = getNextRegularNumber(number, path, False)
    leftPath = getNextRegularNumber(number, path, True)
    if len(rightPath):
        number = replace(number, rightPath, getNumber(number, rightPath)+rightNumber)
    if len(leftPath):
        number = replace(number, leftPath, getNumber(number, leftPath)+leftNumber)
    number = replace(number, path, 0)
    return number


def split(number, path):
    numberToSplit = getNumber(number, path)
    return replace(number, path, [math.floor(numberToSplit/2), math.ceil(numberToSplit/2)])

def reduce(number):
    requiredOperation = 69
    while requiredOperation:
        [requiredOperation, path] = getRequiedOperation(number)
        if requiredOperation == 1:
            number = explode(number, path)
        if requiredOperation == 2:
            number = split(number, path)
    return number

def add(numberA, numberB):
    numberToReduce = [numberA, numberB]
    return reduce(numberToReduce)

def calculateMagnetude(number):
    if type(number) == int:
        return number
    numberPartOne = number[0]
    numberPartTwo = number[1]
    return calculateMagnetude(numberPartOne) * 3 + calculateMagnetude(numberPartTwo) * 2

numbers = [json.loads(number) for number in lines]

result = add(numbers[0], numbers[1])
for number in numbers[2:]:
    result = add(result, number)

print(calculateMagnetude(result))