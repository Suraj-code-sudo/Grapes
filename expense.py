for _ in range(1):
    a, b = map(int, input().split())
    salary = 2**b
    for i in range(1,a+1):
        salary = salary/2
    print(int(salary))