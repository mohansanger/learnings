"""def makePreeti(Func):
    def inner():
        print("I got decorated")
        Func()
    return inner

def ordinary():
    print("I am ordinay function")

decoratedFun=makePreeti(ordinary)
decoratedFun()

"""
#Another way to define decorators in py

def make_pretty(func):
    def inner():
        print("i am decorated")
        func()
    return inner

@make_pretty #ordinaly=make_prety(ordinary)
def ordinary():
    print("I am ordinary")

ordinary()


#Samrt divite function

def smart_divide(func):
    def inner(a,b):
        print("i am going to divide ", a , "and", b)
        if b==0:
            print("woops! can't divede")
            return
        return func(a,b)
    return inner
@smart_divide
def div(a,b):
    print(a/b)

div(4,2)
div(2,0)


