import os

input = [61,17]

outputs = {}

with open(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt", "r") as f:
    instructions = f.read().split("\n")

def giveToBot(bots, givingBotId, takingBotId, chipvalue, toOutput):
    if not toOutput:
        if takingBotId in bots:
            bots[takingBotId].append(chipvalue)
        else:
            bots[takingBotId] = [chipvalue]
    else:
        outputs[takingBotId] = chipvalue
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
    bots = giveToBot(bots, -1, int(parts[-1]), int(parts[1]), False)

botInstructions = {}

for botInstructionRaw in botInstructionsRaw:
    parts = botInstructionRaw.split(" ")
    botId = int(parts[1])
    lowId = (int(parts[6]), parts[5] == "output")
    highId = (int(parts[11]), parts[10] == "output")
    botInstructions[botId] = (lowId, highId)

bots = {key: val for key, val in sorted(bots.items(), key = lambda ele: len(ele[-1]), reverse=True)}


while len(bots[list(bots)[0]]) > 1:
    currentBot = list(bots)[0]
    """ print(botInstructions[currentBot]) """
    lowBot = botInstructions[currentBot][0][0]
    lowBotOutput = botInstructions[currentBot][0][1]
    highBot = botInstructions[currentBot][1][0]
    highBotOutput = botInstructions[currentBot][1][1]
    bots = giveToBot(bots, currentBot, lowBot, min(bots[currentBot]), lowBotOutput)
    bots = giveToBot(bots, currentBot, highBot, max(bots[currentBot]), highBotOutput)
    bots = {key: val for key, val in sorted(bots.items(), key = lambda ele: len(ele[-1]), reverse=True)}

print(outputs[0]*outputs[1]*outputs[2])