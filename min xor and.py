import math
for _ in range(1):
    minimum = []
    n = int(input())
    lis = input().split()
    lis = [int(x) for x in lis]
    lis.sort()
    for i in range(n-1):
            minimum.append((lis[i])^(lis[i+1]))
    print(min(minimum))
            
            