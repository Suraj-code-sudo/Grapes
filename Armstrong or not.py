n=eval(input("Enter the number to check whether it is a Armstromg or not : "))
rem=0
arm=0
a=n
while(a>0):
    rem=a%10
    arm=arm+(rem**3)
    a=a//10
if(arm==n):
    print("You Entered is value is a Armstrong Number !!")
else:
    print("Sorry !! Entered value is not a Armstrong Number !!")

