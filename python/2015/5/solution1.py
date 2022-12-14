lines = [x.strip() for x in open("input.txt")]

vowels = "aeiou"
bannedCombinations = ["ab", "cd", "pq", "xy"]

def countVowels(word):
    return sum([word.count(vowel) for vowel in vowels])

def checkDouble(word):
    for i, letter in enumerate(word[:-1]):
        if letter == word[i+1]:
            return True
    return False

def hasBannedCombination(word):
    for bannedCombination in bannedCombinations:
        if word.count(bannedCombination):
            return True
    return False

def checkIfNice(word):
    return countVowels(word) >= 3 and checkDouble(word) and not hasBannedCombination(word)

""" for line in lines:
    print(line) """

print([checkIfNice(word) for word in lines].count(True))