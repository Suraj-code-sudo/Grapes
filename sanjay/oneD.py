def oneDimension(array, n):
    return [(x) for x in array if x>n]

input_list = list(map(int, input().split()))
n = int(input())

result = oneDimension(input_list, n)
print(result)