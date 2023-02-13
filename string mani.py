string = "abc"
lis1 = []
lis1[:0] = string
lis2 = []
for i in range(len(lis1)):
    for j in range(i):
        str1 = ""
        lis1[i], lis1[j] = lis1[j], lis1[i]
        for ele in lis1:
            str1 += ele
        lis2.append(str1)
        str1 = str1[::-1]
        if str1 not in lis2:
            lis2.append(str1)
print(lis2)