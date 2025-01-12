n=int(input("Enter the Factorial Number:"))


def factorial(n):
    Result=1
    for i in range(1,n+1):
     Result *=i
    return Result
print(f"Factorial Numner of {n} is {factorial(n)}")

import random
print(random.randrange(10,30))
l1=[1,2,3,4]
print(random.choices(l1))
print(random.choice(l1))
random.shuffle(l1)
print(l1)
print(random.random())
