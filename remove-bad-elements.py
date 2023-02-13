nums = list(map(int, input().split()))
dic = {}

for i in nums:
    dic[i] = nums.count(i)

keys = [x for x in dic.keys()] 
values = [x for x in dic.values()]

max_count = max(values)
print(len(nums)-max_count)