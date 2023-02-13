dit = {}
in_list = []
for _ in range(int(input())):
    in_list.append(input())
count = 1
for i in range(0, len(in_list)):
    for j in range(i+1, len(in_list)):
        if in_list[i] == in_list[j]:count+=1
    if in_list[i] not in dit.keys():
        dit[in_list[i]] = count
        count = 1
lis = []
for key, values in dit.items():
    lis.append(values)
print(len(lis))
str_val = ""
for i in lis:
    str_val = str_val+str(i)+str(" ")
print(str_val)