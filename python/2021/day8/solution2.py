def removeIfNotIncludes(arr, mustContain):
    output = []
    for content in mustContain:
        if content in arr:
            output.append(content)
    return output

def removeFromArr(arr, remove):
    output = []
    for content in arr:
        if content != remove:
            output.append(content)
    return output

def sevenSegmentToInt(display):
    if display[0]:
        #0,2,3,5,6,7,8,9
        if display[1]:
            #0,5,6,8,9
            if display[2]:
                #0,8,9
                if display[3]:
                    #8,9
                    if display[4]:
                        #8
                        return 8
                    else:
                        #9
                        return 9
                else:
                    #0
                    return 0
            else:
                #5,6
                if display[4]:
                    #6
                    return 6
                else:
                    #5
                    return 5
        else:
            #2,3,7
            if display[3]:
                #2,3
                if display[4]:
                    #2
                    return 2
                else:
                    #3
                    return 3
            else:
                #7
                return 7
    else:
        #1,4
        if display[1]:
            #4
            return 4
        else:
            #1
            return 1

solution = 0

lines = [x.strip() for x in open("input.txt")]

allData = []

allLetters = ["a","b","c","d","e","f","g"]

for line in lines:
    allData.append([y.split(" ") for y in line.split(" | ")])

for data in allData:
    possibleConnections = {"a":allLetters.copy(),"b":allLetters.copy(),"c":allLetters.copy(),"d":allLetters.copy(),"e":allLetters.copy(),"f":allLetters.copy(),"g":allLetters.copy()}
    for signal in data[0]:
        #eindeutig
        if len(signal) == 2:
            for connection in ["c","f"]:
                possibleConnections[connection] = removeIfNotIncludes(possibleConnections[connection],[letter for letter in signal])
        if len(signal) == 3:
            for connection in ["a","c","f"]:
                possibleConnections[connection] = removeIfNotIncludes(possibleConnections[connection],[letter for letter in signal])
        if len(signal) == 4:
            for connection in ["b","c","d","f"]:
                possibleConnections[connection] = removeIfNotIncludes(possibleConnections[connection],[letter for letter in signal])

        #mehrdeutig
        if len(signal) == 5:
            for connection in ["a","d","g"]:
                possibleConnections[connection] = removeIfNotIncludes(possibleConnections[connection],[letter for letter in signal])
        if len(signal) == 6:
            for connection in ["a","b","f","g"]:
                possibleConnections[connection] = removeIfNotIncludes(possibleConnections[connection],[letter for letter in signal])

    #aus den anderen möglichkeiten entfernen, fals es bereits eindeutig etwas anderem zugeordnet ist:
    for i in range(3):
        for letter in allLetters:
            if len(possibleConnections[letter]) == 1:
                for key in possibleConnections:
                    if key != letter:
                        possibleConnections[key] = removeFromArr(possibleConnections[key],possibleConnections[letter][0])
    
    DAfINALsOLUTION = {}

    for key in possibleConnections:
        DAfINALsOLUTION[possibleConnections[key][0]] = key


    #get the real output
    numberStr = ""
    for output in data[1]:
        realDisplay = [False]*7
        for letter in output:       
            realDisplay[allLetters.index(DAfINALsOLUTION[letter])] = True
        numberStr += str(sevenSegmentToInt(realDisplay))
    solution += int(numberStr)

print(solution)
    

#0:- 1:- 2:1 3:7 4:4 5:2,3,5 6:0,6,9 7:8