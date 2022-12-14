from dataclasses import field
import os
import copy

fieldY = 50
fieldX = 6

with open(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt", "r") as f:
    instructions = f.read().split("\n")

def printDisplay(display):
    print()
    for row in display:
        for field in row:
            print("#" if field else ".", end="")
        print()
    print()

def rect(display, dimensions):
    for y in range(dimensions[0]):
        for x in range(dimensions[1]):
            display[x][y] = True
    return display

def rotateColumn(display, instructions):
    global filedX
    column = "".join(["#" if row[instructions[0]] else "." for row in display])
    for rowId in range(len(display)):
        offset = rowId-instructions[1]
        offset = offset if offset > -1 else offset+fieldX
        display[rowId][instructions[0]] = column[offset] == "#"
    return display

def rotateRow(display, instructions):
    global fieldY
    row = "".join(["#" if x else "." for x in display[instructions[0]]])
    for columnId in range(len(display[0])):
        offset = columnId-instructions[1]
        offset = offset if offset > -1 else offset+fieldY
        display[instructions[0]][columnId] = row[offset] == "#"
    return display

display = []

for x in range(fieldX):
    line = []
    for y in range(fieldY):
        line.append(False)
    display.append(line)

printDisplay(display)

for instruction in instructions:
    if "rect" in instruction:
        display = rect(display, [int(x) for x in instruction.split(" ")[-1].split("x")])
    if "column" in instruction:
        display = rotateColumn(display, [int(x) for x in instruction.split("x=")[-1].split(" by ")])
    if "row" in instruction:
        display = rotateRow(display, [int(x) for x in instruction.split("y=")[-1].split(" by ")])

printDisplay(display)

print(sum([row.count(True) for row in display]))