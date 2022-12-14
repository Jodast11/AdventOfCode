passwordList = [[word for word in line.strip().split(" ")] for line in open("input.txt","r")]

def checkIfValid(password):
    passwordParts = [[letter for letter in word] for word in password]
    for passwordPart in passwordParts:
        passwordPart.sort()
    if len(passwordParts) == len(list(set(["".join(passwordPart) for passwordPart in passwordParts]))):
        return True
    return False

print([checkIfValid(password) for password in passwordList].count(True))