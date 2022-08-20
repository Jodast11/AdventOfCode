import math

def doOpperations(input):
    registers = "wxyz"

    variables = [0,0,0,0]

    inputs = [1,3,5,7,9,2,4,6,8,9,9,9,9,9]

    for instruction in input:
        parameters = instruction.split(" ")
        if len(parameters) > 2:
            if parameters[2] in registers:
                parameters[2] = variables[registers.index(parameters[2])]
            else:
                parameters[2] = int(parameters[2])

        if "inp" in parameters:
            variables[registers.index(parameters[1])], inputs = getInput(inputs)
        if "add" in parameters:
            variables[registers.index(parameters[1])] += parameters[2]
        if "mul" in parameters:
            variables[registers.index(parameters[1])] *= parameters[2]
        if "div" in parameters:
            variables[registers.index(parameters[1])] = math.floor(variables[registers.index(parameters[1])] / parameters[2])
        if "mod" in parameters:
            variables[registers.index(parameters[1])] %= parameters[2]
        if "eql" in parameters:
            variables[registers.index(parameters[1])] = int(variables[registers.index(parameters[1])] == parameters[2])

    print(variables[3])

def getInput(inputs):
    return inputs[0], inputs[1:]

input = [line.strip() for line in open("input.txt").readlines()]

doOpperations(input)

