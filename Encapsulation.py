#make it private and don't alow full access ot it

class Encap:
    __name="MOhan"

    def __init__(self):
        print(self.__name)
        self.__display()
        
    def __display(self):
       print("Hello")

obj=Encap()
