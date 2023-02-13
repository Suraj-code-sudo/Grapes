try:
    for _ in range(int(input())):
        a, b, c = map(int, input().split())
        print(max(a+c, b))
except:
    pass