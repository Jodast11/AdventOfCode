import re

def isRealTrinagle(triangle):
    triangle.sort()
    return triangle[0] + triangle[1] > triangle[2]

inputFile = open("input.txt").read()
inputTable = [[int(entry) for entry in line.lstrip().split(" ")] for line in re.sub(" +", " ", inputFile).split("\n")]

triangles = []
for i in range(3):
    for row in 