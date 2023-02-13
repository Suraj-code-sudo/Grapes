try:
    for _ in range(int(input())):
        n, w = map(int, input().split())
        array = input().split()
        j=1
        array.sort()
        array.reverse()
        print(array)
        k = int(array[0])
        for i in array:
            if int(i) >= w:
                print(n-1)
                break
        else:
            while(j<=len(array)):
                k+=int(array[j])
                if k >= w:
                    print(n-j-1)
                    break
                else:
                    j+=1
except:
    pass