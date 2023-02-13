x =0
y =0
z = 0
for _ in range(int(input())):
    tmp = list(map(int, input().split()))
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    m = list(map(int, input().split()))

    for i in range(tmp[0]):
        print("Im")
        x = p[i]+x
        y = c[i]+y
        z = m[i]+z
        if x == y and y == z and x == z:
            print(x)
            break
