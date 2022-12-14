class logicGate:
    def __init__(self, type, connections) -> None:
        self.type = type
        self.connections = connections

connections = {}
solvedConnections = {}

def clean(inp):
    if inp.isdigit():
        return int(inp)
    else:
        return inp

def getValue(startPoint):
    if startPoint in solvedConnections.keys():
        return solvedConnections[startPoint]

    print(solvedConnections)

    if type(startPoint) == int:
        return startPoint

    if type(connections[startPoint]) == int:
        solvedConnections[startPoint] = connections[startPoint]
    elif type(connections[startPoint]) == str:
        solvedConnections[startPoint] = getValue(connections[startPoint])
    else:
        if connections[startPoint].type == "NOT":
            solvedConnections[startPoint] = ~getValue(connections[startPoint].connections[0])
        elif connections[startPoint].type == "OR":
            solvedConnections[startPoint] = getValue(connections[startPoint].connections[0])|getValue(connections[startPoint].connections[1])
        elif connections[startPoint].type == "AND":
            solvedConnections[startPoint] = getValue(connections[startPoint].connections[0])&getValue(connections[startPoint].connections[1])
        elif connections[startPoint].type == "LSHIFT":
            solvedConnections[startPoint] = getValue(connections[startPoint].connections[0])<<getValue(connections[startPoint].connections[1])
        elif connections[startPoint].type == "RSHIFT":
            solvedConnections[startPoint] = getValue(connections[startPoint].connections[0])>>getValue(connections[startPoint].connections[1])

    return solvedConnections[startPoint]

connectionsRaw = [x.strip() for x in open("input.txt")]

for connectionRaw in connectionsRaw:
    parts = connectionRaw.split(" ")
    destination = parts[-1]
    if len(parts) == 3:
        connections[destination] = clean(parts[0])
    elif len(parts) == 4:
        connections[destination] = logicGate(parts[0], [parts[1]])
    else:
        connections[destination] = logicGate(parts[1], [clean(parts[0]), clean(parts[2])])

connections["b"] = 46065

print(getValue("a"))