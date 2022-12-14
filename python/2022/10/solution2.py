programm = open("input.txt").read().split("\n")
screen = []

def executeCycleOperation(currentCycle, x):
    global screen
    vertPos = (currentCycle-1) % 40
    screen.append("#" if (vertPos >= x-1 and vertPos <= x+1) else ".")

def printScreen(screen):
    lines = [screen[i*40:(i*40)+40] for i in range(6)]
    for line in lines:
        print("".join(line))

x = 1
currentCycle = 0

for instruction in programm:
    currentCycle += 1
    executeCycleOperation(currentCycle, x)
    if "a" in instruction:
        currentCycle += 1
        executeCycleOperation(currentCycle, x)
        x += int(instruction.split(" ")[-1])

printScreen(screen)
print()