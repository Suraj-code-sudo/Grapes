list=[]
n=int(input("Enter the number of values to be inserted : "))
for i in range(0,n):
    a=int(input("Enter the value : "))
    list.append(a)
print(list)

list.sort()
search=eval(input("Enter the search element : "))
beg=0
las=len(list)
while(beg <= las):
    mid=(beg+las)//2
    if (search == list[mid]):
        print(mid)
        break
    elif(beg<list[mid]):
        las=mid-1
    else:
        beg=mid+1