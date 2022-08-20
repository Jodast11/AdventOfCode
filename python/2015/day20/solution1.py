input = 290000000

def calcPresentsGot(houseNr):
    presentsCollected = 0
    for elfId in range(houseNr,0,-1):
        if houseNr % elfId == 0:
            presentsCollected += elfId * 10
    return presentsCollected

def getPrimeNumbers(lower, upper): #hippity hoppity
    numbers = []
    for num in range(lower, upper + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                numbers.append(num)
    return numbers

primeNumbers = getPrimeNumbers(0,10000)


factors = 1

# while input not in primeNumbers:
#     for number in primeNumbers:
#         if input % number == 0:
#             input = int(input/number)
#             factors *= number
#             break
#     print(input)

# print(factors)
print(calcPresentsGot(29000000))

# 249022800 too high
# 744131100 too high