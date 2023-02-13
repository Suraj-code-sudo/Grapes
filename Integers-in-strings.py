A = "1,2,3"

result = []
for x in A:
    if x != ',':
        result.append(int(x))

print(result)