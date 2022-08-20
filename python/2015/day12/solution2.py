import json

input = [x.strip() for x in open("input.txt")][0]

jsonInput = json.loads(input)

def calculateSum(jsonObject):
    result = 0
    contentType = type(jsonObject)
    if contentType == dict:
        for key in jsonObject:
            recivedResult, foundRed = calculateSum(jsonObject[key])
            if foundRed: 
                return 0, False
            else:
                result += recivedResult
    elif contentType == list:
        for listContent in jsonObject:
            recivedResult, foundRed = calculateSum(listContent)
            result += recivedResult
    elif contentType == str:
        if jsonObject == "red":
            return 0, True
    elif contentType == int:
        result += jsonObject
    else:
        print(contentType)
    return result, False


print(calculateSum(jsonInput))

