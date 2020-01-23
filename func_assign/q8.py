import random

def uel(l1):
 
    r1 = []
    print(l1)
    for i in l1:
        if (i in r1):
            continue
        r1.append(i)
    return r1

list1 = [random.randint(1,10) for i in range(12)]
list2 = uel(list1)
print(list2)

