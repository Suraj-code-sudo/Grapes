n=int(input("enter"))
list=[]
for i in range(0,n):
    a=int(input("Enter"))
    list.append(a)
b=int(input("Enter"))
flag=0
for i in range(0,n):
    if (list[i]==b):
        print("Element found at ",i)
        flag=1
if(flag!=1):
    print("Not found")
