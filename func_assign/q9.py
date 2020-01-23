import random

def isprim(num):
    for i in range(1,num//2):
        if (num%i == 0):
            return f"not a prime {num}"
    return f"a prime number {num}"

print(isprim(random.randint(1,10000)))
