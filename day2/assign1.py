import copy

l1 = [*range(1,11)]
l2 = [*range(15,21)]

l3 = copy.copy(l1)
l3[2] = 12

print(f"list 1:{l1}\nlist 3:{l3}")

l4 = copy.deepcopy(l2)

#l2[3] = 9
l4[3] = 8
print(f"list 2: {l2}\nlist 4: {l4}")

for i in range(20,26):
    l4.append(i)
print(l4)

l4.pop()
print(l4)

l3.extend(range(30,36))
print(l3)

l3.remove(12)
print(l3)

l4.insert(0,67)
print(l4)

l3[4:3]=[*range(90,93)]
print(l3)
