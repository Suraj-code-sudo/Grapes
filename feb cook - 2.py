try:
    for _ in range(1):
        n, w = 5, 10
        #n, w = int(input())
        #array = input().split(' ')zaaaaaaaaa
        array = ['3', '2', '6', '1', '3']
        for i in array:
            if(int(i) >= w):
                print(n-1)
                break
            for j in range(int(i)):    
                if(int(i) >= w):
                    print(n-2)
                    break
                lis.append(int(i)+array[j])
        if(max(lis) < w):
            for x in array:
                if(max(lis)+int(x) >= w):
                    print(n-3)
                
except:
    pass