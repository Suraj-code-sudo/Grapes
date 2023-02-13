class stu():
    __ref ="Helloo"
    def __init__(self,sub,mar):
        self.sub=sub
        self.mar=mar
    def get(self,color):
        self.color=color
        return color
    def __repr__(self):
        return "First %s"%(self.sub)
fun=stu("Hlo","Bye")
print(fun.sub)
print(fun._stu__ref)
a=input("entr : ")

fun2=stu(a,"90")
print(fun2.sub)
print(fun2.mar)
print(fun2.get("red"))
print([fun2])