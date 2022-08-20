with open("Input.txt") as f: #open the imput file
    lines = [x for x in f.read().split("\n")] #split its lines and save it into lines

cycles = 3

#lst3d = [[["." for cc1 in range(len(lines)+((cycles-1)*2))] for cc2 in range(len(lines)+((cycles-1)*2))] for cc2 in range(len(lines)+((cycles-1)*2))]
lst3d = [[["." for cc1 in range(25)] for cc2 in range(25)] for cc2 in range(25)]

def fillInput():
    for i in range(len(lines)):
        for a in range(len(lines[i])):
            lst3d[int((len(lst3d)-1)/2)-int(len(lines)/2)+1][int((len(lst3d)-1)/2)-int(len(lines)/2)+i][int((len(lst3d)-1)/2)-int(len(lines)/2)+a] = lines[i][a]
            #print(lines[i][a])
        #print()

def print3dList(lst):
    for i in range(len(lst[0][0])):
        print("Slice "+str(i)+":")
        for a in range(len(lst[0])):
            print(lst[i][a])
    print()
    print()
    
def findSuroundingActive(x,y,z):
    activeCounter=0
    for i in range(-1,2):
        for a in range(-1,2):
            for e in range(-1,2):
                if i!=0 or a!=0 or e!=0:
                    if i+x >= 0 and a+y >= 0 and e+z >= 0 and i+x < len(lst3d) and a+y < len(lst3d) and e+z < len(lst3d):
                        if lst3d[i+x][a+y][e+z] == "#":
                            activeCounter+=1
    return activeCounter 
 
def copyList(lst):
    #lstCopy = [[["." for cc1 in range(len(lines)+((cycles-1)*2))] for cc2 in range(len(lines)+((cycles-1)*2))] for cc2 in range(len(lines)+((cycles-1)*2))]
    lstCopy = [[["." for cc1 in range(25)] for cc2 in range(25)] for cc2 in range(25)]
    for i in range(len(lst)):
        for a in range(len(lst[i])):
            for e in range(len(lst[i][a])):
                lstCopy[i][a][e] = lst3d[i][a][e]
    return(lstCopy)
                

def cycle():
    lst3dcopy = copyList(lst3d)
    for i in range(len(lst3d)):
        for a in range(len(lst3d[i])):
            for e in range(len(lst3d[i][a])):
                if lst3d[i][a][e] == "#":
                    if findSuroundingActive(i,a,e) == 2 or findSuroundingActive(i,a,e) == 3:
                        lst3dcopy[i][a][e] = "#"
                    else:
                        print("Changing2")
                        lst3dcopy[i][a][e] = "."
                if lst3d[i][a][e] == ".":
                    if findSuroundingActive(i,a,e) == 3:
                        print("Changing3")
                        lst3dcopy[i][a][e] = "#"
                    else:
                        lst3dcopy[i][a][e] = "."
    return lst3dcopy
                        

def findAmountOfActive():
    activeCounter=0
    for i in range(len(lst3d)):
        for a in range(len(lst3d[i])):
            for e in range(len(lst3d[i][a])): 
                if lst3d[i][a][e] == "#":
                    activeCounter+=1
    return activeCounter
                

fillInput()
print3dList(lst3d)
for i in range(6):
    lst3d = cycle()
      
print(findAmountOfActive())

