n = int(input())
array = list(input().split())
array = sorted(array)
sum = 0
for var in array:
    sum+=int(var)
for i in array:
    if int(i)*n > sum:
        print(int(i))
        break