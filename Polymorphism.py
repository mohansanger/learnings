#Overloading and overiding, same function name with with diffrent signature 

list=[1,2,3,4,5]
str="mohan"
print(len(list), len(str))

#----------Function Overloading(same name with diffenrt parameter-------------
#----------Same function giving two diffrent output---------

class Overloading:
    def display(self,name=""):
        print("Hello "+name)

obj=Overloading()
obj.display()
obj.display("Hanu")

#Fnction Overriding , CLass A function will be override, chile function override with parent function
#overriding can be skip with Super() function
class A:
    def display(self):
        print("WHat's Up")
class B(A):
    def display(self):
        super().display()
        print("How are you!!")
obj=B()
obj.display()