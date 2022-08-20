with open("Input.txt") as f: #open the imput file
    lines = [x for x in f.read().split("\n")] #split its lines and save it into lines
         
log = open("Spam.spam", "a")    
    
lines_cleaned = []
lines_cleaned_inter = []
lines_cleaned_orig = []

def printLayout(var):
    for x in var:
        log.write(x)
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
    
    
def occupiIfArroundEmpty(x,y):
    global lines_cleaned
    global lines_cleaned_inter
    line_orig = lines_cleaned_inter[x]
    if lines_cleaned_orig[x][y] == "L":
        if getSeatsInViewOccupied(x,y) == 0:
            line = line_orig[:y]+"#"+line_orig[y+1:]
            return line
    return line_orig
            
def leaveIfArroundIsOccupied(x,y):
    global lines_cleaned
    global lines_cleaned_inter
    line_orig = lines_cleaned_inter[x]
    if lines_cleaned_orig[x][y] == "#":
        #print(getSeatsInViewOccupied(x,y))
        if getSeatsInViewOccupied(x,y) >= 5:
            line = line_orig[:y]+"L"+line_orig[y+1:]
            return line
    return line_orig
    

def getSeatsInViewOccupied(x,y):
    global lines_cleaned_orig
    counter = 0
    i = 0
    for x_shift in range(-1,2):
        for y_shift in range(-1,2):
            #print("X Shift: "+str(x_shift)+" Y Shift: "+str(y_shift))
            for i in range(1,1000):
                if x+(x_shift*i) < 0 or y+(y_shift*i) < 0 or x+(x_shift*i)>len(lines_cleaned_orig)-1 or y+(y_shift*i) > len(lines_cleaned_orig[x+(x_shift*i)])-1:
                    #print("Breaking! XCord = "+str(x+(x_shift*i))+" YCord = "+str(y+(y_shift*i)))
                    break  
                if x_shift != 0 or y_shift != 0:
                    #print("X: "+str(x+(x_shift*i))+" Y: "+str(y+(y_shift*i)))
                    if lines_cleaned_orig[x+(x_shift*i)][y+(y_shift*i)] == "#":
                        counter += 1
                        #print("Found #")
                        break
                    if lines_cleaned_orig[x+(x_shift*i)][y+(y_shift*i)] == "L":
                        #print("Found L")
                        break
    return counter

clean_field()
print()


lines_check = []

while True:

    #print("Entering:")
    for i in range(1,len(lines_cleaned)-1):
        for a in range(1,len(lines_cleaned[i])-1):
            lines_cleaned_inter[i] = occupiIfArroundEmpty(i,a)
    lines_cleaned_orig = lines_cleaned_inter[:]

    printLayout(lines_cleaned_orig)

    #print()
    #print("Leaving:")
    for i in range(1,len(lines_cleaned)-1):
        for a in range(1,len(lines_cleaned[i])-1):
            lines_cleaned_inter[i] = leaveIfArroundIsOccupied(i,a)

    lines_cleaned_orig = lines_cleaned_inter[:]
    

    
    printLayout(lines_cleaned_orig)
    if lines_check == lines_cleaned_orig:
        break
    lines_check = lines_cleaned_orig[:]
    #print()
    
counter = 0    
for i in range(1,len(lines_cleaned_orig)-1):
    for a in range(1,len(lines_cleaned_orig[i])-1):
        if lines_cleaned_orig[i][a] == "#":
            counter += 1
            
print("The solution is: "+str(counter))

log.close()
