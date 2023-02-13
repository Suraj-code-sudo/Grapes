from itertools import product
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))
c = sorted(product(a, b))
s = ""
for i in c:
    s += " "+str(i)
print(s)