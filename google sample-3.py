import math
for case in range(1):
    N = int(input())
    array = input().split()
    n_c = math.ceil(N/2)
    lis = []
    j=2
    for i in range(1, n_c+1):
        for _ in range(j):
            lis.append(i)
        j+=1
    values = lis[:N]
    string = ""
    for x in values:
        string = string+str(x)+""
    
    final_string = "Case #"+str(case+1)+":"
    print(final_string, string)


