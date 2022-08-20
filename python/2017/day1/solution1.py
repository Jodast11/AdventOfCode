digits = [line for line in open("input.txt","r").read().split("\n")[0]]

def solveCaptcha(digits):
    result = 0
    for index, digit in enumerate(digits):
        if digit == digits[(index+1)%len(digits)]:
            result += int(digit)
    return result

print(solveCaptcha(digits))