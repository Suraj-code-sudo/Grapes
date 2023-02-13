t = int(input())
for i in range(t):
    try:
        a, b = map(int, input().split())
        try:
            print(int(a / b))
        except ZeroDivisionError as e:
            print("Error Code :", e)

    except ValueError as v:
        print("Error Code :", v)
