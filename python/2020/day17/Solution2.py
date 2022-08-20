with open("Input.txt") as f: #open the imput file
    lines = [x for x in f.read().split("\n")] #split its lines and save it into lines

length = 25

lst4d = [[[["." for cc1 in range(length)] for cc2 in range(length)] for cc2 in range(length)] for cc2 in range(length)]

def print4dList(lst):
    for i in range(len(lst[0][0][0])):
        for a in range(len(lst[0][0])):
            print("Slice "+str(i)+","+str(a)+":")
            for e in range(len(lst[0])):
                print(lst[i][a][e])
                print()
    print()
    print()
    
    
def fillInput():
    for i in range(len(lines)):
        for a in range(len(lines[i])):
            lst4d[int((len(lst4d)-1)/2)-int(len(lines)/2)+1] [int((len(lst4d)-1)/2)-int(len(lines)/2)+1][int((len(lst4d)-1)/2)-int(len(lines)/2)+i] [int((len(lst4d)-1)/2)-int(len(lines)/2)+a] = lines[i][a]
            #print(lines[i][a])
        #print()
        
def findSuroundingActive(x,y,z,w):
    activeCounter=0
    for i in range(-1,2):
        for a in range(-1,2):
            for e in range(-1,2):
                for o in range(-1,2):
                    if i!=0 or a!=0 or e!=0 or o!=0:
                        if i+x >= 0 and a+y >= 0 and e+z >= 0 and o+w >= 0 and i+x < len(lst4d) and a+y < len(lst4d) and e+z < len(lst4d) and o+w < len(lst4d):
                            if lst4d[i+x][a+y][e+z][o+w] == "#":
                                activeCounter+=1
    return activeCounter 
        
def copyList(lst):
    #lstCopy = [[["." for cc1 in range(len(lines)+((cycles-1)*2))] for cc2 in range(len(lines)+((cycles-1)*2))] for cc2 in range(len(lines)+((cycles-1)*2))]
    lstCopy = [[[["." for cc1 in range(length)] for cc2 in range(length)] for cc2 in range(length)] for cc2 in range(length)]
    for i in range(len(lst)):
        for a in range(len(lst[i])):
            for e in range(len(lst[i][a])):
                for o in range(len(lst[i][a][e])):
                    lstCopy[i][a][e][o] = lst4d[i][a][e][o]
    return(lstCopy)   

def findAmountOfActive():
    activeCounter=0
    for i in range(len(lst4d)):
        for a in range(len(lst4d[i])):
            for e in range(len(lst4d[i][a])):
                for o in range(len(lst4d[i][a][e])): 
                    if lst4d[i][a][e][o] == "#":
                        activeCounter+=1
    return activeCounter
    
def cycle():
    lst4dcopy = copyList(lst4d)
    for i in range(len(lst4d)):
        for a in range(len(lst4d[i])):
            for e in range(len(lst4d[i][a])):
                for o in range(len(lst4d[i][a][e])):
                    if lst4d[i][a][e][o] == "#":
                        if findSuroundingActive(i,a,e,o) == 2 or findSuroundingActive(i,a,e,o) == 3:
                            lst4dcopy[i][a][e][o] = "#"
                        else:
                            #print("Changing2")
                            lst4dcopy[i][a][e][o] = "."
                    if lst4d[i][a][e][o] == ".":
                        if findSuroundingActive(i,a,e,o) == 3:
                            #print("Changing3")
                            lst4dcopy[i][a][e][o] = "#"
                        else:
                            lst4dcopy[i][a][e][o] = "."
    return lst4dcopy
    
    
 
fillInput()
#print3dList(lst3d)
for i in range(6):
    lst4d = cycle()
      
print(findAmountOfActive())