import random
numbers=[n**2 for n in range(1,6)]
print(numbers)

random.shuffle(numbers)

print(numbers)
def largest(numbers):
    large=numbers[0]
    for n in numbers:
     if n>large:
      large=n
    return large


print(largest(numbers))


List1=[1,2,3,4,5]

List2=[num*num for num in List1 if num%2==0]

print(List2)

even_Number=[num for num in range(1,15) if num%2==0]
print("Even Numbers:",even_Number)

NumList=[1,2,3,4,5,6]
EvenSeries=["-Even" if i%2==0 else "-Odd" for i in NumList]
print("Even: ",EvenSeries)

word = "Python"
vowels = "aeiou"

result=[char for char in word if char in vowels]
print("vowels: ",result)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

multiplication=[[i*j for j in range(1,6)] for i in range(2,5)]
print("Multiplication:",multiplication)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
mult=[]
for i in range(2,5):
  row=[]
  for j in range(1,6):
    row.append(i*j)
  mult.append(row)
print(mult)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

lamlist=list(map(lambda num: num**2,NumList))
print(lamlist)

greet=lambda : print("Lambda function")
greet()

greet1=lambda name : print("Hi there ",name)
greet1("MOhan")