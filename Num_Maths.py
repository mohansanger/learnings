import random
print(random.randrange(10,30))
l1=[1,2,3,4]
print(random.choices(l1))
print(random.choice(l1))
random.shuffle(l1)
print(l1)
print(random.random())

#Maths Lib
import math

print(math.pi)
print(math.cos(math.pi))
print(math.log(1000))
print(math.factorial(5))

#Area of a circule
radious=5

def calc_area(radious):
    res=math.pi*radious*radious
    return res
print(f"Aread of circule is {round(calc_area(radious),2)}")

#List 
a="xyz"
re=list(a)
print(re[-1])
print(re[-2])
print(re[-3])
re.append("mss")
print(re)
re.insert(0,"kss")
print(re)
num=[1,2,3,4]
re.extend(num)
print(re)

for i in re:
    print(f"Items:{i}")

print(re.sort())