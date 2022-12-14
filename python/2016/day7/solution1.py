import os
import re

with open(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt", "r") as f:
    ipAddresses = f.read().split("\n")

def hasAutonomousBridgeBypassAnnotation(sequence):
    for i in range(len(sequence)-3):
        if sequence[i:i+2] == sequence[i+2:i+4][::-1] and sequence[i] != sequence[i+1]:
            return True
    return False

def checkIp(ip):
    invertedReqirement = False
    foundAutonomousBridgeBypassAnnotation = False
    parts = re.split(r'\[|\]', ip)
    for part in parts:
        if hasAutonomousBridgeBypassAnnotation(part):
            if invertedReqirement:
                return False
            else:
                foundAutonomousBridgeBypassAnnotation = True
        invertedReqirement = not invertedReqirement
    return foundAutonomousBridgeBypassAnnotation

count = 0
for ip in ipAddresses:
    if checkIp(ip):
        count += 1

print(count)