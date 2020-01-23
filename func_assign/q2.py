import random

def sumList(list1):
    sum = 0
    for iter1 in list1:
        sum += iter1
    return sum

list1=[random.randint(1,100) for i in range(5)]

print(sumList(list1))
