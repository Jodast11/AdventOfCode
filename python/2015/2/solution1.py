with open("input.txt") as f:
    input = f.readlines()

total = 0

def getBoxSurface(length, width, height):
    surfaces = [length * width, width * height, length * height]
    return(2*surfaces[0]+2*surfaces[1]+2*surfaces[2]+min(surfaces))

dimensions = [[]]
for line in input:
    dimensions.append([int(y) for y in line.replace("\n","").split("x")])

for dimension in dimensions:
    try:
        #print(getBoxSurface(dimension[0],dimension[1],dimension[2]))
        total += getBoxSurface(dimension[0],dimension[1],dimension[2])
    except:
        print("Error")
    
print(total)
