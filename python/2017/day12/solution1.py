connections = [connection.strip() for connection in open("input.txt","r").readlines()]

zeroConnections = [0]
prevLength = 0

while len(zeroConnections) != prevLength:
    prevLength = len(zeroConnections)
    for connection in connections:
        interconnectedProgramms = []
        partA, partB = connection.split(" <-> ")
        interconnectedProgramms.append(int(partA))
        for x in partB.split(", "):
            interconnectedProgramms.append(int(x))
        
        for program in interconnectedProgramms:
            if program in zeroConnections:
                for programX in interconnectedProgramms:
                    if programX not in zeroConnections:
                        zeroConnections.append(programX)
                continue       

print(len(zeroConnections)) 