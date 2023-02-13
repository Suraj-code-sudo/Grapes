list=[]
n=int(input("Enter the number of values to be inserted : "))
for i in range(0,n):
    a=int(input("Enter the value : "))
    list.append(a)
print(list)
m=0
for i in list:
    if m<i:
        m=i

print(m)