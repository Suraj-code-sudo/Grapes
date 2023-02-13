string = "aabbbccde"
temp = {}
for i in range(len(string)):
    c = string.count(string[i])
    if (string[i]) not in temp.keys():
        temp[string[i]] = c

print(temp)
    
for key,value in temp.items():


