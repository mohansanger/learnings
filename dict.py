capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
print(capitals)
d1 = {"Fruit":["Mango","Banana"], "Flower":["Rose", "Lotus"]}
d2 = {('India, USA'):'Countries', ('New Delhi', 'New York'):'Capitals'}
print (d1)
print (d2)
#Type error as key can't be as key , as its mutable 
#d3 = {["Mango","Banana"]:"Fruit", "Flower":["Rose", "Lotus"]}
#print (d3)


#Deuplicate keys in dict:
d4 = {"Fruit":"Banana","Flower":"Rose", "Fruit":"Mango", "Flower":"Lotus", "Fruit":"Apple","Fruit":"Avacodo","Flower":"Sunflower"}
print(d4)

student_info = dict(name="Alice", age=21, major="Computer Science")

#acces dict value using [] and inside its key
print("Dictionary using dict():",student_info["name"])  
#acces dict value usingget method and key as param
print("Get Method:",student_info.get("major"))

####################################Modifying Dictionary Items######################################
student_info["name"]="Mohan Singh"
#add items
student_info["City"]="Agra"
print("Dictionary using dict():",student_info) 

#___________________________Removing Items_________________________________
#remove items using the del statement, the pop() method, or the popitem()

#Del
del student_info["age"]
print("Dictionary using dict():",student_info) 

#POP()
student_info.pop("City")
print("Dictionary using dict():",student_info)
#popItem() dont take any argument delete from the last 

student_info.popitem()
print("Dictionary using dict():",student_info)

#iterate through the keys, values, or key-value pairs in a dictionary using loops 

student_info = {
   "name": "Alice",
   "age": 22,
   "major": "Computer Science",
   "graduation_year": 2023
}
# Iterating through keys
for key in student_info:
    print(f"Keys:{key}:{student_info[key]}")
# Iterating through values
for value in student_info.values():
    print(f"Values:",value)
# Iterating through key-value pairs
for key, value in student_info.items():
    print(f"Key:{key} : value:{value}")

#Python Dictionary Operators , Union "|"
d1 = {"Fruit":["Mango","Banana"], "Flower":["Rose", "Lotus"]}
d2 = {('India, USA'):'Countries', ('New Delhi', 'New York'):'Capitals'}
d3=d1|d2
print("Union of 2 dict:",d3)

d1|=d2
print("Union of 2 dict:",d1)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Python Dictionary Methods@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
print("D3:",d3.clear())
print("D1:",d1.copy())

#FromKeys()
x=("key1","key2","key3")

#print("FRom Keys:",dict.fromkeys(x,5))

#dict.has_key(key)
#print("Rsut:",d1.__hash__("key1"))

# Initializing key-value pairs
d = {2: 56, 1: 2, 3: 323,4:1}

##   print((i,d[i]),end=" ")

#sort dict by value 

short_items=sorted(d.items(),key= lambda  item : item[1] )
print(short_items)