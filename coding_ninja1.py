k = 4
arr = [7, 9, 4, 1]
max_arr = sorted(arr)
max_arr = list(reversed(max_arr))
value = max_arr[k-1]
print(arr.index(value))
