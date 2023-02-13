lis = [2,4,6,6,4,2,4]
l_set = set(lis)
trip = 0
valid = 0

for i in l_set:
    if lis.count(i) == 2 or lis.count(i)== 3:
        trip = trip+1
        valid = 1
    else:
        valid = 0
        break
if valid:print(trip)
else:print(-1)

