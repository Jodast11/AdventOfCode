import os

input = [61,17]

with open(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt", "r") as f:
    instructions = f.read().split("\n")

def giveToBot(bots, givingBotId, takingBotId, chipvalue):
    if takingBotId > -1:
        if takingBotId in bots:
            bots[takingBotId].append(chipvalue)
        else:
            bots[takingBotId] = [chipvalue]
    if givingBotId > -1:
        bots[givingBotId].pop(bots[givingBotId].index(chipvalue))
    return bots

initalInstructions = []
botInstructionsRaw = []

for instruction in instructions:
    if "value" in instruction:
        initalInstructions.append(instruction)
    else:
        botInstructionsRaw.append(instruction)

bots = {}

for initalInstruction in initalInstructions:
    parts = initalInstruction.split(" ")
    bots = giveToBot(bots, -1, int(parts[-1]), int(parts[1]))

botInstructions = {}

for botInstructionRaw in botInstructionsRaw:
    parts = botInstructionRaw.split(" ")
    botId = int(parts[1])
    lowId = int(parts[6]) if parts[5] != "output" else -1
    highId = int(parts[11]) if parts[10] != "output" else -1
    botInstructions[botId] = (lowId, highId)

bots = {key: val for key, val in sorted(bots.items(), key = lambda ele: len(ele[-1]), reverse=True)}


while len(bots[list(bots)[0]]) > 1:
    currentBot = list(bots)[0]
    if bots[currentBot] == input or bots[currentBot] == input[::-1]:
        print(currentBot)
        break
    lowBot = botInstructions[currentBot][0]
    highBot = botInstructions[currentBot][1]
    bots = giveToBot(bots, currentBot, lowBot, min(bots[currentBot]))
    bots = giveToBot(bots, currentBot, highBot, max(bots[currentBot]))
    bots = {key: val for key, val in sorted(bots.items(), key = lambda ele: len(ele[-1]), reverse=True)}
