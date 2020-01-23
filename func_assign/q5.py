import random
import sys

def fact(num):
    if (num == 0 or num == 1):
        return 1
    elif (num > 1):
        return num*fact(num-1)
    else:
        return "Not a +ve integer. "

if (len(sys.argv) == 2):
    num = int(sys.argv[1])
else:
    num = random.randint(-5,10)

print(fact(num))
