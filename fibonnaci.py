#Generators
def fibonnaci():
    a,b=0,1
    while True:
        a,b=b,a+b
        yield a

fib=fibonnaci()
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))

