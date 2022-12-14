directions = [direction for direction in open("input.txt","r").readlines()[0].strip().split(",")]

totalNorth = directions.count("n") + directions.count("ne") + directions.count("nw")
totalSouth = directions.count("s") + directions.count("se") + directions.count("sw")
totalEast = directions.count("se") + directions.count("ne")
totalWest = directions.count("sw") + directions.count("nw")

horizontalMovement = totalNorth - totalSouth if totalNorth > totalSouth else totalSouth - totalNorth
verticalMovement = totalEast - totalWest if totalEast > totalWest else totalWest - totalEast

print(max([horizontalMovement, verticalMovement]))