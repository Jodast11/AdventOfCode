with open("Input.txt") as f:
    parts = f.read().split("\n\n")

deck1_str = parts[0].replace("Player 1:\n","").split("\n")
deck2_str = parts[1].replace("Player 2:\n","").split("\n")    

deck1 = []
deck2 = []

for string in deck1_str:
    deck1.append(int(string))
    
for string in deck2_str:
    deck2.append(int(string))       
       
       
def getCard(card, deck):
    deckNew = []
    for i in range(1,len(deck)):
        deckNew.append(deck[i])
    deckNew.append(deck[0])
    deckNew.append(card)
    return deckNew
    
def loseCard(deck):
    deckNew = []
    for i in range(1,len(deck)):
        deckNew.append(deck[i])
    return deckNew

roundNr = 1
    
while len(deck1) > 0 and len(deck2) > 0:
    print(f"-- Round {roundNr} --")
    print(f"Player1's deck: {deck1}")
    print(f"Player2's deck: {deck2}")
    print(f"Player 1 plays: {deck1[0]}")
    print(f"Player 2 plays: {deck2[0]}")
    roundNr+=1
    
    if deck1[0] > deck2[0]:
        deck1 = getCard(deck2[0], deck1)
        deck2 = loseCard(deck2)
        print("Player 1 wins the round!")
    else:
        deck2 = getCard(deck1[0], deck2)
        deck1 = loseCard(deck1)
        print("Player 2 wins the round!")
        
    print()
        
print("== Post-game results ==")
print(f"Player 1's deck: {deck1}")
print(f"Player 2's deck: {deck2}")

result = 0

if len(deck1) > 0:
    counter = len(deck1)
    for i in range(len(deck1)):
        result += (deck1[i]*counter)
        counter -= 1
        
if len(deck2) > 0:
    counter = len(deck2)
    for i in range(len(deck2)):
        result += (deck2[i]*counter)
        counter -= 1
        
print(result)
        

