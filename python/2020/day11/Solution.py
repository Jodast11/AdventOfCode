with open("Test.txt") as f: #open the imput file
    lines = [x for x in f.read().split("\n")] #split its lines and save it into lines
         
    
lines_cleaned = []
lines_cleaned_inter = []
lines_cleaned_orig = []

def printLayout(var):
    for x in var:
         print(x)
         

def clean_field():
    global lines_cleaned
    global lines_cleaned_inter
    global lines_cleaned_orig
    length = len(lines[0])
    empty_line = "."*length
    
    lines.insert(0,empty_line) #insert an empty line at the beginning, so that we dont get an error
    lines.append(empty_line) #insert an empty line at the end, so that we dont get an error
    for x in lines:
        line = "."+x[0:]+"."
        lines_cleaned.append(line)
    
    lines_cleaned_orig = lines_cleaned[:]
    lines_cleaned_inter = lines_cleaned[:]
    
    printLayout(lines_cleaned)
    lines_cleaned_inter = lines_cleaned



def getSeatsArroundOccupied(x,y):
    global lines_cleaned
    global lines_cleaned_orig
    counter = 0
    for i in range(-1,2):
        for a in range(-1,2):
            #print("Checking: "+str(x+i)+" "+str(x+a)+" : "+lines_cleaned[x+i][x+a])
            if i != 0 or a != 0:
                if lines_cleaned_orig[x+i][y+a] == "#":
                    counter += 1
    return counter
    
def occupiIfArroundEmpty(x,y):
    global lines_cleaned
    global lines_cleaned_inter
    line_orig = lines_cleaned_inter[x]
    if lines_cleaned_orig[x][y] == "L":
        if getSeatsArroundOccupied(x,y) == 0:
            line = line_orig[:y]+"#"+line_orig[y+1:]
            return line
    return line_orig
            
def leaveIfArroundIsOccupied(x,y):
    global lines_cleaned
    global lines_cleaned_inter
    line_orig = lines_cleaned_inter[x]
    if lines_cleaned_orig[x][y] == "#":
        if getSeatsArroundOccupied(x,y) >= 4:
            line = line_orig[:y]+"L"+line_orig[y+1:]
            return line
    return line_orig


clean_field()
print()

lines_check = []

while True:

    print("Entering:")
    for i in range(1,len(lines_cleaned)-1):
        for a in range(1,len(lines_cleaned[i])-1):
            lines_cleaned_inter[i] = occupiIfArroundEmpty(i,a)
    lines_cleaned_orig = lines_cleaned_inter[:]

    printLayout(lines_cleaned_orig)

    print()
    print("Leaving:")
    for i in range(1,len(lines_cleaned)-1):
        for a in range(1,len(lines_cleaned[i])-1):
            lines_cleaned_inter[i] = leaveIfArroundIsOccupied(i,a)

    lines_cleaned_orig = lines_cleaned_inter[:]
            
    printLayout(lines_cleaned_orig)
    if lines_check == lines_cleaned_orig:
        break
    lines_check = lines_cleaned_orig[:]
    print()
    
counter = 0    
for i in range(1,len(lines_cleaned_orig)-1):
    for a in range(1,len(lines_cleaned_orig[i])-1):
        if lines_cleaned_orig[i][a] == "#":
            counter += 1
print("The solution is: "+str(counter))