def func(name, age):
    print(name, age)
    age+=1
    func(name, age)
print(func("ROSE", 14)) 