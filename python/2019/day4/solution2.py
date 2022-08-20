input = [int(x) for x in "271973-785961".split("-")]

validPasswordsCount = 0

for possiblePassword in range(input[0],input[1]):
    possiblePasswordStr = str(possiblePassword)
    #two adjacent same
    if True in [possiblePasswordStr[i] == possiblePasswordStr[i+1] for i in range(len(possiblePasswordStr)-1)]:
        #number increasing
        if False not in [possiblePasswordStr[i] <= possiblePasswordStr[i+1] for i in range(len(possiblePasswordStr)-1)]:
            #one double (not tripple)
            index = 0
            nrCounts = []
            prevChar = 69
            while index < len(possiblePasswordStr):
                if possiblePasswordStr[index] == prevChar:
                    nrCounts[-1] += 1
                else:
                    nrCounts.append(1)
                    prevChar = possiblePasswordStr[index]
                index += 1
            if 2 in nrCounts:
                validPasswordsCount += 1


print(validPasswordsCount)