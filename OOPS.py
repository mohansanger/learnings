"""class demo:
    a=10

    def sumvalue(self):
        print(20+30)

obj=demo()
print(obj.a)
print(obj.sumvalue())
"""
class demo1:
    a=10
    def showvalue(self):
        self.c=self.a*self.a
        print(self.c)
    def showvalue1(self,a,b):
        print(a+b)

obj1=demo1()
obj1.showvalue1(2,4)


class demo2:
    def __init__(self) -> None:
        print("Jai Shre Ram") 
obj2=demo2()       

#Single Inheritance

class A:
    def displayA(self):
        print("This is class A")

class B(A):#(A):
    def displayB(self):
        print("This is class B")

"""InheritanceObj=B()
InheritanceObj.displayA()
InheritanceObj.displayB()"""
#---------------Multiple Inheritance--------------

class C(B):#(A,B):

    def displayC(self):
        print("This is class C")

#print("Multileve lInheritance")

"""InheritanceObj1=C()
InheritanceObj1.displayA()
InheritanceObj1.displayB()
InheritanceObj1.displayC()"""


#-------------Multileve Inheritance---------------
Inh=C()
Inh.displayA()
Inh.displayB()
Inh.displayC()