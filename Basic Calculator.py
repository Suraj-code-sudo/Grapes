def add(x,y):
    add=x+y
    return add
def sub(x,y):
    sub=x-y
    return sub
def mul(x,y):
     mul=x*y
     return mul
def div(x,y):
    div=x/y
    rem=x%y
    return div,rem
print("1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division")
n=eval(input("Choose the choice number of the Operation : "))
a=eval(input("Enter the Value : "))
b=eval(input("Enter the Value : "))
if(n==1):
    m=add(a,b)
    print("\nThe  Sum is ",m)
elif(n==2):
    n=sub(a,b)
    print("\nThe  Difference is ",n)
elif(n==3):
    o=mul(a,b)
    print("\nThe Multiplied Value is",o)
elif(n==4):
    p,q=div(a,b)
    print("\nThe Quotient is ",p)
    print("The Remainder is ",q)
