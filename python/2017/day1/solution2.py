digits = [line for line in open("input.txt","r").read().split("\n")[0]]

def solveCaptcha(digits):
    result = 0
    for index, digit in enumerate(digits):
        if digit == digits[(index+int(len(digits)/2))%len(digits)]:
            result += int(digit)
    return result

print(solveCaptcha(digits))