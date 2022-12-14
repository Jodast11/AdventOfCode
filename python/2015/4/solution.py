import hashlib
import time

key = "ckczppom"
startTime = time.time()

i = 0

while True:
    if hashlib.md5((key + str(i)).encode()).hexdigest()[:5] == "00000":
        print(i)
        break
    i += 1