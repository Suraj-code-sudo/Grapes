for _ in range(int(input())):
    n,k = map(int, input().split())
    s = input()
    p = -1
    max = ""
    for i in range(n):
        if max<s[i]:
            max = s[i]
            d = i
        elif max == s[i]:
            p = i-d
            break
        s = s[1:] + s[:1]
    if p == -1:print(d+(k-1)*n)
    else:print(d+(k-1)*p)
    print("")
    