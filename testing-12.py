lis = []
lis_2 = []
    
string = ['a', 'b', 'c']
for i in range(len(string)):
    for j in range(i):
        string[j], string[i] = string[i], string[j]
        ori_str = ''.join(map(str, string))
        if ori_str not in lis:
            lis.append(ori_str)
        string.reverse()
        rev_str = ''.join(map(str, string))
        if rev_str not in lis:
            lis.append(rev_str)
print(lis)