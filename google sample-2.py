for case in range(int(input())):
    kingdom = input()
    last = kingdom[-1]
    string = "Case #"
    vowels = ['a', 'e', 'i', 'o', 'u']
    if (last not in vowels) and (last != 'y'):
        print(string+str(case+1)+":",kingdom, "is ruled by Bob.")
    elif (last in vowels) and (last != 'y'):
        print(string+str(case+1)+":",kingdom, "is ruled by Alice.")
    elif (last == 'y'):
        print(string+str(case+1)+":",kingdom, "is ruled by nobody.")
