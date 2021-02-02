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

while(nString >= 0):
    s = ""
    while(sLen > 0):
        s += random.choice(string.ascii_letters + string.digits)
        sLen -= 1
    nString -= 1
    sLen = int(sys.argv[2])
    print(s)