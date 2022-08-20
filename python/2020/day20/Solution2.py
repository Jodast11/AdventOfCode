

with open("Input.txt") as f:
    parts = f.read().split("\n\n")

tile_id_map = {}

tiles = []

tiles_cleaned = []

first_row = []

columns = []

final_id_map = []

final_image = []

final_image_monsters = []
    
#print(parts)

for part in parts:
    tiles_int = []
    lines = part.split("\n")
    tile_id_map.update({len(tile_id_map) : int(lines[0][lines[0].index("Tile ")+5:len(lines)-2])})
    for i in range(1,len(lines)):
        tiles_int.append(lines[i])
    tiles.append(tiles_int)
        
        
def findEdges(tile_nr):
    edges = []
    edge1 = ""
    edge2 = ""
    for char in tiles[tile_nr]:
        edge1 = edge1+char[0]
        edge2 = edge2+char[len(char)-1]
    edges.append(edge1)
    edges.append(tiles[tile_nr][0])
    edges.append(edge2)
    edges.append(tiles[tile_nr][len(tiles[tile_nr])-1])
    return edges 
    
def findUniqueEdges(tile_nr):
    edges = findEdges(tile_nr)
    counter = 0
    unique_counter = 0
    for edge in edges:
        for i in range(len(tiles)):
            if edge in findEdges(i) or edge [::-1] in findEdges(i):
                counter += 1
        #print(counter)
        if counter == 1:
            unique_counter+=1
        counter = 0
    return unique_counter
       

def findFittingTiles(tile_nr):
    edges = findEdges(tile_nr)
    fittingTiles = [-1,-1,-1,-1,]
    for counter, edge in enumerate(edges):
        for i in range(len(tiles)):
            if edge in findEdges(i) or edge [::-1] in findEdges(i):
                if i != tile_nr:
                    fittingTiles[counter] = i
                    break
    return fittingTiles

def printTile(tile_nr):
        for line in tiles[tile_nr]:
            print(line)
            
def printArr(arr):
    for line in arr:
            print(line)
            
def flip(arr, axis): #1: vertikal 2: horizontal 3: garnicht
    if axis == 1:
        out_arr = []
        for line in arr:
            out_arr.append(line [::-1])
        return out_arr
    if axis == 2:
        out_arr = arr[:]
        for counter, line in enumerate(arr):
            out_arr[len(out_arr)-1-counter] = line
        return out_arr
    return arr
    

def rotate(in_arr, rot_nr):
    out_arr = []
    tmp_str = ""
    tmp = zip(*in_arr [::-1])
    for line in tmp:
        for nr in line:
            tmp_str = tmp_str+nr
        out_arr.append(tmp_str)
        tmp_str = ""
    if rot_nr == 1:
        return out_arr
    else:
        return rotate(out_arr, rot_nr-1)


def moveUntilTopRowIs(tile_nr, row):
    if tiles[tile_nr][0] == row:
        return
    for i in range(1,4):
        for a in range(1,5):
            if flip(rotate(tiles[tile_nr],a),i)[0] == row:
                tiles[tile_nr] = flip(rotate(tiles[tile_nr],a),i)
                return
                
def getLeftColumnOfArr(arr):
    out = ""
    for line in arr:
        out = out+line[0]
    return out
    
def getRightColumnOfArr(arr):
    out = ""
    for line in arr:
        out = out+line[len(line)-1]
    return out
                
def moveUntilLeftColumnIs(tile_nr, column):
    if getLeftColumnOfArr(tiles[tile_nr]) == column:
        return
    for i in range(1,4):
        for a in range(1,5):
            if getLeftColumnOfArr(flip(rotate(tiles[tile_nr],a),i)) == column:
                tiles[tile_nr] = flip(rotate(tiles[tile_nr],a),i)
                return               
               
        

def make_first_row(start_tile, last_row):
    if start_tile == -1:
        return
    first_row.append(start_tile)
    #print(start_tile)
    fitting = findFittingTiles(start_tile)
    #print(fitting)
    #print(tiles[start_tile][len(tiles[start_tile])-1])
    moveUntilTopRowIs(fitting[3], tiles[start_tile][len(tiles[start_tile])-1])
    fitting = findFittingTiles(start_tile)
    #print(fitting)
    #printArr(tiles[fitting[3]])
    make_first_row(fitting[3], tiles[start_tile][len(tiles[start_tile])-1])


def make_column(start_tile, last_column):
    if start_tile == -1:
        return
    columns.append(start_tile)
    fitting = findFittingTiles(start_tile)
    moveUntilLeftColumnIs(fitting[2], getRightColumnOfArr(tiles[start_tile]))
    fitting = findFittingTiles(start_tile)
    make_column(fitting[2], getRightColumnOfArr(tiles[start_tile]))

def removeLocationData():
    tile_tmp = []
    for tile in tiles:
        for counter, line in enumerate(tile):
            if counter != 0 and counter != len(line)-1:
                tile_tmp.append(line[1:-1])
        tiles_cleaned.append(tile_tmp)
        tile_tmp = []
            
            
    
def makeImage():
    global columns 
    global final_image
    make_first_row(17, tiles[17][len(tiles[17])-1])
    for  start in first_row:
        make_column(start, getRightColumnOfArr(tiles[start]))
        final_id_map.append(columns)
        columns = []
    removeLocationData()
    line_tmp = ""
    for row in range(12):
        for line in range(8):
            for tile_id in final_id_map[row]:
                line_tmp = line_tmp + tiles_cleaned[tile_id][line]
            final_image.append(line_tmp)
            line_tmp = ""
    #printArr(lines)

def findSeaMonsters(arr):
    global final_image_monsters 
    final_image_monsters = arr[:]
    counter = 0
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            try:
                if arr[y][x] == "#":
                    if arr[y+1][x+1] == "#":
                        #print("Found Until Position 1")
                        if arr[y+4][x+1] == "#":
                            if arr[y+5][x] == "#":
                                if arr[y+6][x] == "#":
                                    if arr[y+7][x+1] == "#":
                                        #print("Found Until Position 2")
                                        if arr[y+10][x+1] == "#":
                                            if arr[y+11][x] == "#":
                                                if arr[y+12][x] == "#":
                                                    if arr[y+13][x+1] == "#":
                                                        #print("Found Until Position 3")
                                                        if arr[y+16][x+1] == "#":
                                                            if arr[y+17][x] == "#":
                                                                if arr[y+18][x] == "#":
                                                                    if arr[y+19][x] == "#":
                                                                        if arr[y+18][x-1] == "#":
                                                                            #print("MONSTER! At: "+str(y)+" "+str(x))
                                                                            counter+=1
                                                                            final_image_monsters[y] = final_image_monsters[y][:x]+"0"+final_image_monsters[y][x+1:]
                                                                            final_image_monsters[y+1] = final_image_monsters[y+1][:x+1]+"0"+final_image_monsters[y+1][x+1+1:]
                                                                            
                                                                            final_image_monsters[y+4] = final_image_monsters[y+4][:x+1]+"0"+final_image_monsters[y+4][x+1+1:]
                                                                            final_image_monsters[y+5] = final_image_monsters[y+5][:x]+"0"+final_image_monsters[y+5][x+1:]
                                                                            final_image_monsters[y+6] = final_image_monsters[y+6][:x]+"0"+final_image_monsters[y+6][x+1:]
                                                                            final_image_monsters[y+7] = final_image_monsters[y+7][:x+1]+"0"+final_image_monsters[y+7][x+1+1:]
                                                                            
                                                                            final_image_monsters[y+10] = final_image_monsters[y+10][:x+1]+"0"+final_image_monsters[y+10][x+1+1:]
                                                                            final_image_monsters[y+11] = final_image_monsters[y+11][:x]+"0"+final_image_monsters[y+11][x+1:]
                                                                            final_image_monsters[y+12] = final_image_monsters[y+12][:x]+"0"+final_image_monsters[y+12][x+1:]
                                                                            final_image_monsters[y+13] = final_image_monsters[y+13][:x+1]+"0"+final_image_monsters[y+13][x+1+1:]
                                                                            
                                                                            final_image_monsters[y+16] = final_image_monsters[y+16][:x+1]+"0"+final_image_monsters[y+16][x+1+1:]
                                                                            final_image_monsters[y+17] = final_image_monsters[y+17][:x]+"0"+final_image_monsters[y+17][x+1:]
                                                                            final_image_monsters[y+18] = final_image_monsters[y+18][:x]+"0"+final_image_monsters[y+18][x+1:]
                                                                            final_image_monsters[y+19] = final_image_monsters[y+19][:x]+"0"+final_image_monsters[y+19][x+1:]
                                                                            final_image_monsters[y+18] = final_image_monsters[y+18][:x-1]+"0"+final_image_monsters[y+18][x:]
                                                                           
                                                                            
                                                                            
            except:
                pass
    #printArr(final_image_monsters)
    #print(counter)            


makeImage()

findSeaMonsters(final_image)

#printArr(final_image)

counter = 0
for line in final_image_monsters:
    for char in line:
        if char == "#":
            counter+=1
            
print(counter)





    
    
            
       

