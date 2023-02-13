prices = [7,1,6,5,4,3,2]
max = 0
i = prices[0]
for j in prices[1:]:
    if j < i:
        i = j
    elif max < j-i:
        max = j-i
        
    

print(max)

