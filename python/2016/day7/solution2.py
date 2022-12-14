import os
import re

with open(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt", "r") as f:
    ipAddresses = f.read().split("\n")

def getAreaBroadcastAccessors(sequence):
    areaBroadcastAccessors = []
    for i in range(len(sequence)-2):
        if sequence[i] == sequence[i+2] and sequence[i] != sequence[i+1]:
            areaBroadcastAccessors.append(sequence[i:i+2])
    return areaBroadcastAccessors

def checkIp(ip):
    parts = re.split(r'\[|\]', ip)
    abs = []
    bas = []
    inverted = False
    for part in parts:
        for x in getAreaBroadcastAccessors(part):
            if inverted:
                bas.append(x)
            else:
                abs.append(x)
        inverted = not inverted
    
    for x in abs:
        if x[::-1] in bas:
            return True
    return False

count = 0
for ip in ipAddresses:
    if checkIp(ip):
        count += 1

print(count)