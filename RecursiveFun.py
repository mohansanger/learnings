def RecursiveFunction(x):
    if x==1:
        return 1
    else:
        return (x * RecursiveFunction(x-1))
    
num=int(input("Enter positive intiger to calculate the factorial number: "))
print(f"Factorial of {num} is  {RecursiveFunction(num)}")
""""
def rec():
    rec()
rec()"""

print(dir())