A = "a12asb34c"
for x in range(len(A)):
    if A[x] not in ['1','2','3','4','5','6','7','8','9','0']:
        A = A.replace(A[x], ',')
A = A.split(',')
res = [int(x) for x in A if x not in [',', '']]
print(sum(res))
