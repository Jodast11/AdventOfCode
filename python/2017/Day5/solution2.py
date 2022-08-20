instructions = [int(instruction) for instruction in open("input.txt","r").readlines()]

steps = 0
stackPointer = 0

while stackPointer < len(instructions):
    jumpDistance = instructions[stackPointer]
    instructions[stackPointer] += -1 if jumpDistance >= 3 else 1
    stackPointer += jumpDistance
    steps += 1

print(steps)