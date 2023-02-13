nums = [1,2,3,4]
result = []
for x in range(1, len(nums)+1):
    result.append(sum(nums[:x]))
print(result)