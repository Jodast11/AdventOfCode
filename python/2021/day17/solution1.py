import threading

def getPositionsVisited(xHigherTarget, yLowerTarget, velocityX, velocityY):
    posX = 0
    posY = 0
    visitedPositions = []
    while posX < xHigherTarget and posY > yLowerTarget:
        posX += velocityX
        posY += velocityY
        velocityY -= 1
        if velocityX > 0:
            velocityX += -1
        if velocityX < 0:
            velocityX += 1
        visitedPositions.append((posY,posX))
    return visitedPositions

def getCordsInArea(xLowerTarget,xHigherTaget,yLowerTarget,yHigherTaget):
    possibleCords = []
    for x in range(xLowerTarget, xHigherTaget+1):
        for y in range(yLowerTarget, yHigherTaget+1):
            possibleCords.append((y,x))
    return possibleCords

def calculateMaxHight(xArea,yArea,start,to,x,areaCords):
    try:
        hights = []

        for xVelocity in range(x):
            for yVelocity in range(start,to):
                # print((xVelocity,yVelocity))
                for cord in getPositionsVisited(xArea[1],yArea[0],xVelocity,yVelocity):
                    if cord in areaCords:
                        # possibleVelocitys.append((xVelocity,yVelocity))
                        hights.append(max([cord[0] for cord in getPositionsVisited(xArea[1],yArea[0],xVelocity,yVelocity)]))
                        break

        print(max(hights))
    except:
        print("None found")

inputParts = [line.strip() for line in open("input.txt").readlines()][0].split(" ")[2:]

xArea = [int(inputParts[0][:-1].split("..")[0][2:]),int(inputParts[0][:-1].split("..")[1])]
yArea = [int(inputParts[1][:-1].split("..")[0][2:]),int(inputParts[1].split("..")[1])]

if xArea[0] > xArea[1]:
    xArea[0], xArea[1] = xArea[1], xArea[0]

if yArea[0] > yArea[1]:
    yArea[0], yArea[1] = yArea[1], yArea[0]

areaCords = getCordsInArea(xArea[0],xArea[1],yArea[0],yArea[1])


# possibleVelocitys = []
# hights = []

# for xVelocity in range(300):
#     for yVelocity in range(-300,300):
#         print((xVelocity,yVelocity))
#         for cord in getPositionsVisited(xArea[1],yArea[0],xVelocity,yVelocity):
#             if cord in areaCords:
#                 # possibleVelocitys.append((xVelocity,yVelocity))
#                 hights.append(max([cord[0] for cord in getPositionsVisited(xArea[1],yArea[0],xVelocity,yVelocity)]))
#                 break

# print(max(hights))

t1 = threading.Thread(target=calculateMaxHight, args=(xArea,yArea,-300,-200,300,areaCords))
t2 = threading.Thread(target=calculateMaxHight, args=(xArea,yArea,-200,-100,300,areaCords))
t3 = threading.Thread(target=calculateMaxHight, args=(xArea,yArea,-100,0,300,areaCords))
t4 = threading.Thread(target=calculateMaxHight, args=(xArea,yArea,0,100,300,areaCords))
t5 = threading.Thread(target=calculateMaxHight, args=(xArea,yArea,100,200,300,areaCords))
t6 = threading.Thread(target=calculateMaxHight, args=(xArea,yArea,200,300,300,areaCords))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()