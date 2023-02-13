sat = [6, 13, 20, 27, 7, 14, 21, 28]
t = int(input())
for _ in range(t):
    c = 0
    n = int(input())
    lis = list(map(int, input().split(' ')))
    for i in lis:
        if i not in sat:
            c+=1
    print(c+8)