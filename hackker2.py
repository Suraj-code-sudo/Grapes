R, C = map(int, input().split())
matrix = []
for _ in range(R):
    matrix.append(list([input()]))
count_list = []
for i in matrix:
    count = 0
    for j in i:
        for k in j:
            if k == "#":
                count += 1
    count_list.append(count)
print(max(count_list))
