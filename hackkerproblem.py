N = int(input())
A = list(map(int,input().split()))
total = sum(A)
avg = A/N
x = floor(avg + 1)
print(x)