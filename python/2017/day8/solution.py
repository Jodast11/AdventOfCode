programm = [line.strip() for line in open("input.txt","r").readlines()]

registers = {}

def getValue(registers, registerName):
    if registerName not in registers:
        return 0
    return registers[registerName]

def checkCondition(condition, registers):
    registerName, opperand, numericValue = condition.split(" ")
    registerValue = getValue(registers, registerName)
    numericValue = int(numericValue)

    if ">" == opperand:
        return registerValue > numericValue
    elif ">=" == opperand:
        return registerValue >= numericValue
    elif "<" == opperand:
        return registerValue < numericValue
    elif "<=" == opperand:
        return registerValue <= numericValue
    elif "!=" == opperand:
        return registerValue != numericValue
    elif "==" == opperand:
        return registerValue == numericValue
    else:
        print(f"Unknown condition {condition}")

def incValue(amount, registerName, registers):
    if registerName in registers:
        registers[registerName] += amount
    else:
        registers[registerName] = amount

def decValue(amount, registerName, registers):
    if registerName in registers:
        registers[registerName] -= amount
    else:
        registers[registerName] = -amount

def applyOperation(operation, registers):
    registerName, opperand, numericValue = operation.split(" ")
    numericValue = int(numericValue)

    if opperand == "dec":
        decValue(numericValue, registerName, registers)
    elif opperand == "inc":
        incValue(numericValue, registerName, registers)
    else:
        print(f"Unknown condition {opperand}")

allTimeMaxValues = []

for instruction in programm:
    operation, condition = instruction.split(" if ")
    if checkCondition(condition, registers):
        applyOperation(operation, registers)
        allTimeMaxValues.append(max([registers[key] for key in registers]))

print(f"Solution 1: {max([registers[key] for key in registers])}")
print(f"Solution 2: {max(allTimeMaxValues)}")