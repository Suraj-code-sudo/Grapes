import math
n = 6
n_c = math.ceil(n/2)
lis = []
j=2
for i in range(1, n_c+1):
    for _ in range(j):
        lis.append(i)
    j+=1
values = lis[:n]
string = ""
for x in values:
    string = string+" "+str(x)
print(string)