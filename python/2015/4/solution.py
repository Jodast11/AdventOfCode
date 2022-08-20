import hashlib
import time

key = "bgvyzdsv"
startTime = time.time()

for i in range(10000000):
    toBeHashed = key + str(i)
    result = hashlib.md5(toBeHashed.encode())
    # if()
    # print(str(result.digest()).replace("\\x","").replace("b'","")[:5])
    if("000000" in str(result.digest()).replace("\\x","").replace("b'","")[:5]):
        print(i)
        break

print("Done in "+str(time.time() - startTime))