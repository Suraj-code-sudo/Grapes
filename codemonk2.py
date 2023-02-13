arr = []
for i in range(3):
    arr.append(list(map(int, input().split())))
for k in range(3):
    for l in range(3):
        for i in range(3):
            for j in range(3):
                print(k,l,"Compare",i,j)