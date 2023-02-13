for case in range(int(input())):
    tot = 0
    N, C = map(int, input().split())
    array = input().split(' ')
    for i in array:
        tot += str(i)
    r_candies = tot % C
    string = "Case #"+str(case+1)+":"
    print(string, r_candies)