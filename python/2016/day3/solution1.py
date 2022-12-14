import re

def isRealTrinagle(triangle):
    triangle.sort()
    return triangle[0] + triangle[1] > triangle[2]

inputFile = open("input.txt").read()
triangles = [[int(y) for y in x.lstrip().split(" ")] for x in re.sub(" +", " ", inputFile).split("\n")]

print([isRealTrinagle(trinagle) for trinagle in triangles].count(True))