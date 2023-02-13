import string
alphabets = [x for x in string.ascii_lowercase]
A = [x for x in A]
B = [x for x in B]
i=0
b_point = True
while b_point:
    if A == B:
        return("".join(A))
    if A[i] != B[i]:
        A[i] = alphabets[(alphabets.index(A[i])+2)%26]
    i=(i+1)%6
