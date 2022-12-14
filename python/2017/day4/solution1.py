passwordList = [[word for word in line.strip().split(" ")] for line in open("input.txt","r")]

def checkIfValid(password):
    if len(password) == len(list(set(password))):
        return True
    return False

print([checkIfValid(password) for password in passwordList].count(True))