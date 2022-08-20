def printCurrentSituaion(currentSituation):
    for line in currentSituation:
        print("".join(line))

def doStep(currentSituation,step):
    print(step)
    # newSituation = [["." for i in range(len(currentSituation[0]))] for j in range(len(currentSituation))]
    newSituation = []
    for line in currentSituation:
        newSituation.append([x for x in "".join(line).replace(">",".")])
    changed = False
    for y, line in enumerate(currentSituation):
        for x, state in enumerate(line):
            if state == ">":
                if currentSituation[y][(x+1)%len(currentSituation[0])] == ".":
                    newSituation[y][(x+1)%len(newSituation[0])] = ">"
                    changed = True
                else:
                    newSituation[y][x] = ">"

    newSituation2 = []

    for line in newSituation:
        newSituation2.append([x for x in "".join(line).replace("v",".")])

    for y, line in enumerate(currentSituation):
        for x, state in enumerate(line):
            if state == "v":
                if newSituation[(y+1)%len(newSituation)][x] == ".":
                    newSituation2[(y+1)%len(newSituation2)][x] = "v"
                    changed = True
                else:
                    newSituation2[y][x] = "v"

    if changed:
        doStep(newSituation2,step+1)
    else:
        print(step+1)


currentSituation = [line for line in open("input.txt","r").read().split("\n")]


doStep(currentSituation,0)