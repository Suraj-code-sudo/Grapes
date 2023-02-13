list=[]
n=int(input("Enter the number of elements to search : "))
for i in range(0,n):
    a=int(input("Enter the elements to add in the list :"))
    list.append(a)
print(list)
x=int(input("enter the number to be searched "))
if x in list:
    print(list.index(x))
else:
    print("Sorry !! Your search element is not found ... !!!")
    
