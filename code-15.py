import math
try:
    for _ in range(int(input())):
        n = int(input())
        lst = list(map(int, input().split()))
        if len(lst) == 1:print(lst[0])
        else:
            s = sum(lst)
            print(math.ceil(s/2))
except:
    pass