lis=['1','2','3','4']
n=4
t = True
for i in range(n):
    l = lis[n-1]
    j=-1
    while j>-(n):
        lis[j] = lis[j-1]
        j-=1
    lis[j] = l
    print(lis)