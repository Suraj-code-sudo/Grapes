n, m = map(int, input().split())
array = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
happy = 0
for i in array:
    if i in A:
        happy += 1
    if i in B:
        happy -= 1
print(happy)