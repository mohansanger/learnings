def add(x,y):
    return x+y

def calculate(func,x,y):
    return func(x,y)

print(calculate(add,2,3))


def greetings(name):
    def greet():
        return "Hello " + name
    return greet

hi=greetings("Mohan") 
print(hi())