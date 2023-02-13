
for _ in range(1):
    N = 5
    K =2
    c=0
    array = '10101'
    array = [x for x in array]
    t=10
    max=0
    while t > 0:
        c+=1
        first = array[0]
        j = 0
        while j < N-1 :
            array[j] = array[j+1]
            j+=1
        array[j] = first
        arr = "".join(array)
        dec = int(arr, 2)
        print(dec)
        if max < dec:
            max = dec
    
        t-=1        
    print(max)