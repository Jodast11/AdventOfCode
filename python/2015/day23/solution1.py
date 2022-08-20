import re

programm = [x.strip() for x in open("input.txt")]

registers = [0,0]

instructionPointer = 0

pattern = re.compile("-?\d+")

def followInstruction():
    global a
    global b
    global instructionPointer
    global programm

    print(programm[instructionPointer])

    if "hlf" in programm[instructionPointer]:
        registerId = 0 if programm[instructionPointer].split(" ")[-1] == "a" else 1
        registers[registerId] = registers[registerId] / 2
        instructionPointer += 1
        return
    if "tpl" in programm[instructionPointer]:
        registerId = 0 if programm[instructionPointer].split(" ")[-1] == "a" else 1
        registers[registerId] = registers[registerId] * 3
        instructionPointer += 1
        return
    if "inc" in programm[instructionPointer]:
        registerId = 0 if programm[instructionPointer].split(" ")[-1] == "a" else 1
        registers[registerId] += 1
        instructionPointer += 1
        return
    if "jmp" in programm[instructionPointer]:
        instructionPointer += int(programm[instructionPointer].split(" ")[-1].replace("+",""))
        return
    if "jie" in programm[instructionPointer]:
        registerId = 0 if programm[instructionPointer].split(" ")[1][:-1] == "a" else 1
        if registers[registerId] % 2 == 0:
            instructionPointer += int(programm[instructionPointer].split(", ")[-1].replace("+",""))
            return
        instructionPointer += 1
        return
    if "jio" in programm[instructionPointer]:
        registerId = 0 if programm[instructionPointer].split(" ")[1][:-1] == "a" else 1
        if registers[registerId] == 1:
            instructionPointer += int(programm[instructionPointer].split(", ")[-1].replace("+",""))
            return
        instructionPointer += 1
        return
try:
    while True:
        followInstruction()
except:
    print(registers)

