#print(dir(locals()["__builtins__"]))


try:
    numerator=10
    denominator=0
   # result=numerator/denominator
   # print(result)

    evenznumber=[2,4,6,8]
    print(evenznumber[5])

except ZeroDivisionError:
    print("Error: Denominator can't be 0")
except IndexError:
    print("Error: Index out of range")

#program to print reciprocal of even number
try:
    num= int(input("Enter intigen Number:"))
    assert num%2==0 
except:
    print("Not an even number")
else:
    reciprocal=1/num
    print(reciprocal)
finally:
    print("Finally Block : Code is ended")