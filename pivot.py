nums = [1,2,3]
left = 0
right = sum(nums)
if sum(nums[1:]) == 0:print(0)
for i in range(len(nums)):
    right -= nums[i]
    if left == right:
        print(i)
    else:
        left += nums[i]