class Element:
    def __init__(self, id):
        self.id = id
        self.nextElement = None
        self.previousElement = None

    def __repr__(self) -> str:
        return f"{self.previousElement.id}->[{self.id}]->{self.nextElement.id}"

loopSize = 256

lengths = [int(length.strip()) for length in open("input.txt","r").readlines()[0].split(",")]

elements = [Element(i) for i in range(loopSize)]

for i, element in enumerate(elements):
    element.nextElement = elements[(i+1) % loopSize]
    element.previousElement = elements[i-1]

skipSize = 0
currentElement = elements[0]

def move(length):
    global currentElement
    for i in range(length):
        currentElement = currentElement.nextElement
    return currentElement

def opperation(length):
    global currentElement
    global skipSize

    a = currentElement.previousElement
    x = currentElement
    currentElement = move(length-1)
    b = currentElement.nextElement
    y = currentElement

    a.nextElement = y
    y.nextElement = a

    lastLoopElement = a

    while currentElement.id != x.id:
        lastLoopElement = currentElement.nextElement
        currentElement.nextElement, currentElement.previousElement = currentElement.previousElement, currentElement.nextElement
        move(1)

    x.previousElement = lastLoopElement
    x.nextElement = b
    b.previousElement = x

    move(1+skipSize)
    skipSize += 1

def getLoop(element, startId=None):
    if startId == element.id:
        return []
    if not startId:
        startId = element.id
    sequence = [element.id]
    for i in getLoop(element.nextElement, startId):
        sequence.append(i)
    return sequence


for length in lengths:
    opperation(length)
    """ print(getLoop(currentElement)) """
    print("x")

print(currentElement.nextElement.id * currentElement.nextElement.nextElement.id)