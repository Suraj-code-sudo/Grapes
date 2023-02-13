string = input()
a = int(0)
k = int(input(""))
s = int(len(string) / k)
for i in range(s):
    temp = string[i*k : (i+1)*k]
    c = ""
    for i in temp:
        if i not in c:
            c+=i
    print(c)