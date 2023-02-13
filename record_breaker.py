T = int(input())
for case in range(T):
    N = int(input())
    lis = [int(v) for v in input().split(" ")]
    max = -1
    records = 0
    for i in range(N):
        first =  lis2[i] > max
        if i+1 < N:
            second_con = lis2[i] > lis2[i+1]
        else:
            second_con = True
        if first and second_con:
            records+=1
        if first:
            max = lis2[i]
    print(f"Case #{case+1}: {records}")

