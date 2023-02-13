nums = [3,2,3]
target = 6
for i in range(0, len(nums)):
    for j in range(i+1, len(nums)):
        print(i,j)
        if nums[i] + nums[j] == target:
            print([i, j])
#    break