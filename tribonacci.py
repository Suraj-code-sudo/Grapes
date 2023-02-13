n = 25
def tribonacci(n):
    i = 0
    j = 1
    k = 1
    if n == 0:  
        return i

    elif n == 1 or n == 2:
        return j
    
    else:
        for _ in range(3, n+1):
            sum = i+j+k
            i = j
            j = k
            k = sum
    print(sum)

tribonacci(n)
            
