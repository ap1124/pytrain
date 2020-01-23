import sys

def cnt(str1):
    ucnt = lcnt = 0 
    for chr1 in str1:
        if (not chr1.isalpha()):
            continue
        else:
            if (chr1.isupper()):
                ucnt += 1
            else:
                lcnt += 1
    return ucnt, lcnt

str1 = ""
if (len(sys.argv) > 1):
    for i in sys.argv:
        if (".py" in i):
            continue
        str1 += i + " " 
else:
    str1 += "A b c d"


print(str1,cnt(str1))
