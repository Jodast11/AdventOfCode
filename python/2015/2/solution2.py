with open("input.txt") as f:
    input = f.readlines()

total = 0

def getSmallestBoxSircomfrance(length, width, height):
    sircomfrances = [(length+width)*2,(height+length)*2,(height+width)*2]
    return(min(sircomfrances))

dimensions = [[]]
for line in input:
    dimensions.append([int(y) for y in line.replace("\n","").split("x")])

for dimension in dimensions:
    try:
        print(getSmallestBoxSircomfrance(dimension[0],dimension[1],dimension[2])+dimension[0]*dimension[1]*dimension[2])
        total += getSmallestBoxSircomfrance(dimension[0],dimension[1],dimension[2])+dimension[0]*dimension[1]*dimension[2]
    except:
        print("Error")
    
print(total)
