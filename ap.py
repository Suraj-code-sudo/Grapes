key = 0
for _ in range(1):
    a,c = map(int, input().split())
    for  i in range(0, c+1):
        if i-a == c-i:
            print(i)
            key=1
            break
        else:
            key=0
if key == 0:
    print(-1)