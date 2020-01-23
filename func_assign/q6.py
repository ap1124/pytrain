import random

def inRange(num,range1):
    if (num in range1):
        return True
    else:
        return False

num = random.randint(-10,16)

range1 = range(-2,7)
print(inRange(num,range1))
