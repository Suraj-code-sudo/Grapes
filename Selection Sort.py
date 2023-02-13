list=[]
n=int(input("Enter the number of values to be inserted : "))
for i in range(0,n):
    a=int(input("Enter the value : "))
    list.append(a)


for i in range(len(list)):
    low=min(list[i:])
    ind=list.index(low)
    list[i],list[ind] = list[ind],list[i]

print(list)