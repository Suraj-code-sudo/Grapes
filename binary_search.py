import time
lis = list(range(1,100000000))
key = 99999999
# lis = [1,2,3,4,5,6,7]
# key = 6
start_time = time.time()
#Linear Search
# for i in lis:
#     if i == key:
#         print("Found")
#         break

# ------------------------------------------------ #

#Binary Search
# mid = 0
# left = 0
# right = len(lis)-1
# check = True
# while(check):
#     mid = int((left+right)/2)
#     if lis[mid] == key:
#         print("found ==> ", mid)
#         break
#     elif lis[mid] > key:
#         right = mid-1
#     else:
#         left = mid+1


print((time.time()) - start_time)