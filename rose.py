lis = [3,4,4,3]
l_set = set(lis)
trip = 0
valid = 0

for i in l_set:
    j = lis.count(i)
    if j==1:
        valid=0
        break
    if j%3 == 0:
        trip += j/3
        valid =1
    elif j%3 == 2:
        trip += (j-2)/3+1
        valid = 1
    else:
        trip += (j-1)/3+1
        valid = 1

if valid:print(trip)
else:print(-1)

