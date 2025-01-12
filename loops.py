val=range(5)
for x in val:
    print(x)

#For Loop with Else

for x in range(5):
    print(x)
else:
    print("No Item Left.")

#Nested For Loop 

for i in range(2):
    for j in range(2):
        print(f"i={i}, j={j}")

#While Loop with else
num=1
while num<=3:
    print(num)
    num+=1
else:
    print("This is else block")

#While with Break
while True:
    user_input=input("Enter you Name: ")
    if user_input=="end":
        print(f"The Loop is Ended")
        break
    print(f"Hi {user_input}")
