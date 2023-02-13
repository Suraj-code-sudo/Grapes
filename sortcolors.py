def sortcolors(nums):
    for i in range(0, len(nums)-1):
        if nums[i] >= nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
    check(nums)
def check(nums):
    for i in range(0, len(nums)-1):
        if nums[i] <= nums[i+1]:continue
        else:sortcolors(nums)
nums = [1,0,2,1,0]
check(nums)
print(nums)