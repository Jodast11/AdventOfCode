def getRingMax(ring):
    ringMax = 1
    for i in range(ring):
        ringMax += 2*((1 + (i*2))+2)+(2*(1 + (i*2)))

    return ringMax

def getRing(number):
    ring = 0
    while getRingMax(ring) < number:
        ring += 1
    return ring

def getRingSize(ring):
    borderLength = (2*ring) + 1
    return (borderLength * borderLength) - ((borderLength-2)*(borderLength-2))

def getCenterNumbers(ring):
    ringStart = getRingMax(ring-1)+1
    centerNumbers = [ringStart + (ring - 1)]
    for i in range(3):
        centerNumbers.append(centerNumbers[-1]+(2*ring))
    return centerNumbers

def getRingCornerNumbers(ring):
    ringCenterNumbers = getCenterNumbers(ring)
    return [number+ring for number in ringCenterNumbers]

def getAdjacentIndexes(index):
    ring = getRing(index)
    prevRingMax = getRingMax(ring-1)
    ringCornerNumbers = getRingCornerNumbers(ring)
    ringStartNumber = prevRingMax+1
    ringSize = getRingSize(ring) 
    prevRingSize = getRingSize(ring-1)
    prevprevRingHight = (2*(ring-2)) + 1
    nextRingSize = getRingSize(ring+1)
    nextRingStartNumber = ringSize+ringStartNumber
    prevRingStartNumber = ringStartNumber-prevRingSize
    nextRingHeight = (2*(ring+1)) + 1

    indexes = []

    if index == ringStartNumber:
        indexes.append(index+1) #1
        indexes.append(index+ringSize+2) # 2
        indexes.append(index+ringSize+1) # 3
        indexes.append(index+ringSize) # 4
        indexes.append(index+ringSize-1) # 5
        indexes.append(index+ringSize-2) # 6
        indexes.append(index-1) #7
        if index == 2:
            indexes.append(4) #8
        else:
            indexes.append(getRingMax(ring-2)+1) #8
        return indexes

    if index < ringCornerNumbers[0]:
        indexes.append(index+1)
        indexes.append(nextRingStartNumber+index-ringStartNumber+2)
        indexes.append(nextRingStartNumber+index-ringStartNumber+1)
        indexes.append(nextRingStartNumber+index-ringStartNumber)
        indexes.append(index-1)
        if getRing(prevRingStartNumber+index-ringStartNumber-2) != ring-1:
           indexes.append(prevRingStartNumber+prevRingSize-1)
        else: 
            indexes.append(prevRingStartNumber+index-ringStartNumber-2)
        indexes.append(prevRingStartNumber+index-ringStartNumber-1)
        indexes.append(prevRingStartNumber+index-ringStartNumber)
        return indexes
    
    if index == ringCornerNumbers[0]:    

        indexes.append(index+ringSize+3) #1
        indexes.append(index+ringSize+2) #2
        indexes.append(index+ringSize+1) #3
        indexes.append(index+ringSize) #4
        indexes.append(index-1) #5
        indexes.append(index-(index-ringStartNumber)-prevRingSize+prevprevRingHight) #6
        indexes.append(index+1) #7
        indexes.append(index+ringSize+4) #8
        return indexes

    if index == ringCornerNumbers[1]:

        indexes.append(nextRingStartNumber+int(nextRingSize/2)-2) #1   
        indexes.append(nextRingStartNumber+int(nextRingSize/2)-3) #2 
        indexes.append(index-1) #3 
        indexes.append(ringStartNumber-prevRingSize+int(prevRingSize/2)-1) #4 
        indexes.append(index+1) #5 
        indexes.append(nextRingStartNumber+int(nextRingSize/2)+1) #6
        indexes.append(nextRingStartNumber+int(nextRingSize/2)) #7 
        indexes.append(nextRingStartNumber+int(nextRingSize/2)-1) #8
        return indexes

    if index == ringCornerNumbers[2]:
        indexes.append(index-1)
        indexes.append(ringStartNumber-prevRingSize+int((prevRingSize/4)*3)-1)
        indexes.append(index+1)
        indexes.append(nextRingStartNumber+(int(nextRingSize/4)*3)+1)
        indexes.append(nextRingStartNumber+(int(nextRingSize/4)*3))
        indexes.append(nextRingStartNumber+(int(nextRingSize/4)*3)-1)
        indexes.append(nextRingStartNumber+(int(nextRingSize/4)*3)-2)
        indexes.append(nextRingStartNumber+(int(nextRingSize/4)*3)-3)
        return indexes

    if index == ringCornerNumbers[3]:
        indexes.append(ringStartNumber)
        indexes.append(index+2)
        indexes.append(index+1)
        indexes.append(nextRingStartNumber+nextRingSize-1)
        indexes.append(nextRingStartNumber+nextRingSize-2)
        indexes.append(nextRingStartNumber+nextRingSize-3)
        indexes.append(index-1)
        indexes.append(ringStartNumber-1)
        return indexes


        

memoryBank = [1]

print(getAdjacentIndexes(27))