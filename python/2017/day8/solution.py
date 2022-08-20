class Instruction:
    def __init__(self, targetRegister, opperation, checkRegister, opperand, number):
        self.targetRegister = targetRegister
        self.opperation = opperation
        self.checkRegister = checkRegister
        self.opperand = opperand
        self.number = number

    def applyOperation(self, checkRegisterValue):
        return self.targetRegister, self.opperation*eval(f"{checkRegisterValue}{self.opperand}{self.number}")
        

rawInstructions = [instruction.strip() for instruction in open("input.txt","r").readlines()]

instructions = []

for rawInstruction in rawInstructions:
    instructionParts = rawInstruction.split(" ")
    instructions.append(Instruction(instructionParts[0], (-1 if instructionParts[1] == "dec" else 1) * int(instructionParts[2]), instructionParts[4], instructionParts[5], int(instructionParts[6])))

allRegisters = {}
maxValue = 0

for instruction in instructions:
    if instruction.targetRegister not in allRegisters:
        allRegisters[instruction.targetRegister] = 0
    if instruction.checkRegister not in allRegisters:
        allRegisters[instruction.checkRegister] = 0

    targetRegister, change = instruction.applyOperation(allRegisters[instruction.checkRegister])
    allRegisters[targetRegister] += change
    if allRegisters[targetRegister] > maxValue:
        maxValue = allRegisters[targetRegister]

print(f"Solution 1: {max(allRegisters.values())}")
print(f"Solution 2: {maxValue}")