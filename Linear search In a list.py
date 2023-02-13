list=[]
n=int(input("Enter the number of values to be inserted : "))
for i in range(0,n):
    a=int(input("Enter the value : "))
    list.append(a)
print(list)


search=eval(input("Enter the search element : "))
for i in range(0,len(list)):
    if search == list[i]:
        print("The element is placed in ", i, "position")
        break
else:
    print("The element is not found")
