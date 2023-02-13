import math
for _ in range(int(input())):
    c=0
    n = int(input())
    for num in range(1,n+1):
        p=1
        q=0
        n_str = str(num)
        for i in n_str:
            q = q+int(i)**4
            p = p*int(i)
        gc = math.gcd(q,p)
        if gc>1:c+=1
    print(c)
    