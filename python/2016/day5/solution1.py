import hashlib

def getPassword(input):
    add = 0
    password = ""
    while len(password) < 8:
        while True:
            if int(hashlib.md5((input+str(add)).encode()).hexdigest()[0:5],16) == 0:
                password += hashlib.md5((input+str(add)).encode()).hexdigest()[5]
                add += 1
                break
            add += 1
    return password

print(getPassword("abbhdwsy"))