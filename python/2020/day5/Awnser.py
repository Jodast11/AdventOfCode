with open("Input.txt") as f:
    lines = f.read()
lines = lines.split("\n")

seats = ["x"]*836
print(seats)

bereichLow = 0 
bereichHigh = 128
bereichLinks = 0 
bereichRechts = 8
higestId = 0

for i in range(len(lines)):
    for a in range(10):
        if lines[i][a] == "F":
            bereichHigh = bereichHigh-((bereichHigh-bereichLow)/2)
        if lines[i][a] == "B":
            bereichLow = bereichLow+((bereichHigh-bereichLow)/2) 
        if lines[i][a] == "L":
            bereichRechts = bereichLinks+((bereichRechts-bereichLinks)/2)           
        if lines[i][a] == "R":
            bereichLinks = bereichRechts-((bereichRechts-bereichLinks)/2) 
        
    #print("Reihe: "+str(bereichLow))
    #print("Sitz: "+str(bereichLinks))
    #print("ID: "+str(bereichLow*8+bereichLinks))
    if (bereichLow*8+bereichLinks) >= higestId:
        higestId=bereichLow*8+bereichLinks
    seats[int(bereichLow*8+bereichLinks)] = "y"
    bereichLow = 0 
    bereichHigh = 128
    bereichLinks = 0 
    bereichRechts = 8

#print("The Highest Id is "+str(higestId))

#print(seats)

for i in range(len(seats)):
    if seats[i] == "x":
        print("Id: "+str(i))

print(seats)



