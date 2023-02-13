A = "fxzabvlglv"
B = [2,7,6,6,2,8]
result = []
for i in B:
    center = A[i-1]
    length = 1
    left = i-2
    right = i
    while(left>=0 and right<len(A)):
        if A[left] ==  A[right]:
            length += 2
            left -= 1
            right += 1
        else:
            break
    result.append(length)
print(result)