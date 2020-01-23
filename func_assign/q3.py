import random

def mulList(list1):
    res = 1
    for iter1 in list1:
        res *= iter1
    return res

list1 = [random.randint(1,10) for i in range(10)]

print(mulList(list1))
