for _ in range(1):
    n, x, c = 5, 5, 2
    
    #A = list(map(int, input().split()))
    A = [1,2,3,4,5]
    sums = []
    cost = 0
    for i in range(len(A)):
        cost+=1
        A = [1,2,3,4,5]
        for j in range(x):
            A[i] = A[i]+j
            print(A)
            sums.append(sum(A)-cost)

    print(sums)
