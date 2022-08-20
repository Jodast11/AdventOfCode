with open("Input.txt") as f:
    parts = f.read().split("\n\n")

tile_id_map = {}

tiles = []
    
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
    edges.append(edge2)
    edges.append(tiles[tile_nr][0])
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
       

solution = 1            
for i in range(len(tiles)): 
    if findUniqueEdges(i) == 2:
        solution *= tile_id_map[i]
        
print(solution)
    

    