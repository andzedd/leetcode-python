import sys
import string
import random

if not len(sys.argv) == 3:
    print("Usage: py random_string.py <number of strings> <string length>")
    sys.exit()

nString = int(sys.argv[1])
sLen = int(sys.argv[2])

if nString <= 0 or sLen <= 0:
    print("Number of strings and length must be greater than 0!")
    sys.exit()

print(''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(sLen)))

while(nString >= 0):
    print(''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(sLen)))
    nString -= 1