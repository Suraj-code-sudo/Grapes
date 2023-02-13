n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4
result = [0,0,0,0]
for i in range(n):
    for j in edges:
        if (j[0] == i or j[1] == i):
            result[i] += j[2]
print(result)
