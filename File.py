with open("app.txt","w",encoding="utf-8") as f:
    wor1=input("Enter the name: ")
    wor2=input("Enter the name: ")
    wor3=input("Enter the name: ")


    f.write("{}\n,{}\n".format(wor1,wor2))
    f.write("Hello")
    o=f.tell()
    print(o)