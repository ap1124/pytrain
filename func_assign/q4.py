
def revStr(str1):
    str2=""
    for iter1 in range(len(str1)):
        str2 += str1[len(str1)-iter1-1]
    return str2

str1 = "1234abcd"

print(str1,revStr(str1))
