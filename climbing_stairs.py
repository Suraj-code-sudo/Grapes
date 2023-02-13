#A = list(map(int, input().split()))
A = [1,1,2,4,1,5,2,5,6]

A[1] = A[0]+A[1]

for i in range(2, len(A)):
    A[i] += min(A[i-1], A[i-2])

print(A[-1])
