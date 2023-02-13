for _ in range(int(input())):
    N, K = map(int, input().split())
    lis = list(map(int, input().split()))
    lis_2 = []
    x = 0
    d = 0
    for i in lis:
        for k in range(i+1, ln(lis)):
            x = i - list[k]
            lis_2.append(x)
        for y in lis_2:
            if y%4 == 0:
               d+=1
            else:d=0




    for j in lis_2:
        if j%K == 0:
            c+=1
    print(c+1)
