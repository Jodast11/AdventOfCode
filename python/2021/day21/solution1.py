playerPositions = [7-1,1-1]
playerScores = [0,0]
player = 0

lastNumberRolled = 0

while playerScores[0] < 1000 and playerScores[1] < 1000:
    diceResult = sum([lastNumberRolled + i for i in range(1,4)])
    lastNumberRolled += 3
    playerPositions[player] = (playerPositions[player] + diceResult) % 10
    playerScores[player] += playerPositions[player] + 1
    player = int(not player)

print(lastNumberRolled * playerScores[player])
