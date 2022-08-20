# with open('input.txt') as file:
#     data = file.readlines()
#     data = [ int(line.strip()) for line in data ]

data = [12092626, 4707356]
    
#print(data)

def findLoop(public_key):
    subject_number = 7
    value = 1
    counter = 0
    while value != public_key:
        value = value*subject_number
        value = value%20201227
        counter += 1        
    return counter
    
def findEncryptionKey(public_key, loop_size):
    value = 1
    for i in range(loop_size):
        value = value*public_key
        value = value%20201227
    return(value)
    
loop_1 = findLoop(data[0])
loop_2 = findLoop(data[1])

print(loop_1)
print(loop_2)

# print(findEncryptionKey(data[0], loop_2))




    