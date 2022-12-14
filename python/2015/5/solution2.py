import re

lines = [x.strip() for x in open("input.txt")]

def checkPairDouble(word):
    for i, letter in enumerate(word[:-1]):
        if letter+word[i+1] in word[:i]+"|"+word[i+2:]:
            return True
    return False

def checkRepeat(word):
    for i, letter in enumerate(word[:-2]):
        if letter == word[i+2]:
            return True
    return False

def checkIfNice(word):
    return checkPairDouble(word) and checkRepeat(word)

print([checkIfNice(word) for word in lines].count(True))