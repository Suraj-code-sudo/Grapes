def Twonum(nums, target):
    j = int(0)
    for i in range(0, len(nums) - 1):
        j = i + 1
        if nums[i] + nums[j] == target:
            print([i, j])
Twonum([2,3,4],5)