#Pass Function

def futureFunction():
    pass

futureFunction()


import math

print(math.sqrt(2))
print(math.pow(2,3))


#defalut args

def message(Hello , hi="Mss"):
    print(Hello , " " + hi)

message("Hello")

#Prime Number Fun

"""n=int(input("Enter Number: "))
def isPrimeNumber(n):
    if n%n==0:
        print(f"{n} is a Prime Number")
    else:
        print(f"{n} is not a Prime Number")

"""
#Python Keyword Argument

def Ayodha(Sita , Ram):
    print(Sita," " + Ram)

Ayodha(Ram= "Ram Ji",Sita="Sita Ji")

#Python Function With Arbitrary Arguments

def sumNum(*num):
    result=0
    for n in num:
        result=result+n
    return result

print(sumNum(1,2,3,4,5,6,7,8,9))




