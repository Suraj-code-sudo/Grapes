nums = [-1,-1,-1,-1,-1,0]
cpy = nums
if sum(nums[1:]) == 0:print(0)
mid = int(len(cpy)/2)

for _ in range(len(nums)):
    if sum(nums[:mid]) == sum(nums[mid+1:]):
        print(mid)
        break
    elif sum(nums[:mid]) >= sum(nums[mid+1:]): mid-=1         
    else: mid+=1
else:
    print(-1)