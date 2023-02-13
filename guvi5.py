#n = int(input())
lis = list(map(int, input().split()))
set_lis = list(set(lis))
count_ = [lis.count(x) for x in set_lis]
for i in range(len(count_)):
    if count_[i]>1:
        print(set_lis[i])