A = [8,6,5,9,7,7,9,3,8]
B = [[3,5,5,5]]

l1 = B[0][0]
r1 = B[0][1]
l2 = B[0][2]
r2 = B[0][3]

l = A[l1-1]
for i in range(l1, r1):
    l = l & A[i]

r_res = A[l2-1]
for i in range(l2, r2):
    r_res = r_res & A[i]

result = l ^ r_res
print(result)
