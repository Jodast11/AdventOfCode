with open("Input.txt") as f:
    data = f.readlines()  #read the Input Data
    data_cleaned = []
    for line in data:   #remove the formating characters
        data_cleaned.append(line.strip())
        
positions = []
positions_unique = []
pointers = []

def findNormalyExecuted(startPos):
    global positions_unique
    global positions
    i = startPos
    while True:
        if i == len(data_cleaned):
            #print("Didnt find any results")
            break
        positions.append(i)
        if "jmp" in data_cleaned[i]:
            #print(data_cleaned[i])
            #print("Jumping from: "+str(i)+" to: "+str(i+int(data_cleaned[i][4:9])))
            if i+int(data_cleaned[i][4:9]) not in positions_unique:
                positions_unique.append(i+int(data_cleaned[i][4:9]))
                findNormalyExecuted(i+int(data_cleaned[i][4:9]))
            break
        #print(data_cleaned[i])
        i += 1


def programEnds(startPos):
    global positions_unique
    i = startPos
    while True:
        if i == len(data_cleaned):
            return True
            break
        if "jmp" in data_cleaned[i]:
            if i+int(data_cleaned[i][4:9]) not in positions:
                positions.append(i+int(data_cleaned[i][4:9]))
                return(programEnds(i+int(data_cleaned[i][4:9])))
            else:
                return False
            break
        i += 1

def tryPossibilitis():
    findNormalyExecuted(0)
    positions.sort()
    for i in range(len(positions)):
        if "jmp" in data_cleaned[positions[i]]:
            print(data_cleaned[positions[i]])
            if programEnds(positions[i]+1):
                return positions[i]


print(tryPossibilitis())

