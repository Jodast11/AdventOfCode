input = 289326

def getXY(pos):
    pass

def getPos(x, y):
    if x > y:
        if x > 0:
            pos = (2*(x-1)+1)*(2*(x-1)+1) + x + y
            print(pos)
        if x < 0:
            pos = ((2*(abs(x)-1)+1)*(2*(abs(x)-1)+1)) + ((2*(abs(x)-1)+2)*2) + abs(x) + (-1 * y)
            print(pos)
    


getPos(1,4)

