n = int(input())
lis = list(map(int, input().split()))
check = 0
for num in lis:
    if num%2 != 0 and num%3 != 0 and num%5 != 0:
        check = 1
        print(0)
        break
if check == 0:print(1)