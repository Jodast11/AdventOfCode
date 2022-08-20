with open("Input.txt") as f: #open the imput file
    lines = [x for x in f.read().split("\n")] #split its lines and save it into lines

buslines=lines[1].split(",")

time = int(buslines[0])
while True:
    validCounter = 0
    for i in range(len(buslines)):
        #print(i)
        if buslines[i] != "x":
            if i == 0:
                if time%int(buslines[i])!=0:
                    #print("breakin")
                    break
                else:
                    validCounter += 1
            else:
                if time%int(buslines[i])!=int(buslines[i])-i:
                    #print("breakin")
                    break
                else:
                    validCounter += 1
        else:
            validCounter += 1
    if validCounter == len(buslines):
        print(time)
        break
    time += int(buslines[0])
    print(time)
         
   

