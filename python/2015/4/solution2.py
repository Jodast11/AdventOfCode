import hashlib
import time

key = "ckczppom"
startTime = time.time()

i = 0

while True:
    if hashlib.md5((key + str(i)).encode()).hexdigest()[:6] == "000000":
        print(i)
        break
    i += 1