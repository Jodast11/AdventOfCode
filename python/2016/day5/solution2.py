import hashlib

def getPassword(input):
    add = 0
    password = [x for x in "00000000"]
    charactersCracked = [0 for i in range(8)]
    while sum(charactersCracked) != 8:
        if int(hashlib.md5((input+str(add)).encode()).hexdigest()[0:5],16) == 0:
            try:
                if charactersCracked[int(hashlib.md5((input+str(add)).encode()).hexdigest()[5],16)] != 1:
                    password[int(hashlib.md5((input+str(add)).encode()).hexdigest()[5],16)] = hashlib.md5((input+str(add)).encode()).hexdigest()[6]
                    charactersCracked[int(hashlib.md5((input+str(add)).encode()).hexdigest()[5],16)] = 1
                
                # print(hashlib.md5((input+str(add)).encode()).hexdigest())
            except:
                pass
        add += 1
    return password

print("".join(getPassword("abbhdwsy")))