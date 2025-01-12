my_dict = {1: "one", 2: "two", 3: "three"}
print(my_dict[1])


#tuple as a key--------List as a key is not allow 
my_dict = {(1, 2): "one two", 3: "three"}
print(my_dict[1,2])

# string as a key, list as a value
my_dict = {"USA": ["Chicago", "California", "New York"]}
print(my_dict["USA"])

dup_dict={1:"a",2:"b",3:"c",1:"d"}
print(dup_dict)



country_capitals = {
  "Germany": "Berlin", 
  "Canada": "Ottawa", 
}

country_capitals["inly"]="rome"
print(country_capitals)

del country_capitals["inly"]
print(country_capitals)

country_capitals.clear()
print(country_capitals)


country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Rome" 
}

for country in country_capitals:
    captial=country_capitals[country]
    print(captial)

print(country_capitals.keys())
print(country_capitals.values())




my_dict = {(1, 2): "one two", 3: "three"}



my_dict1 = {"USA": ["Chicago", "California", "New York"]}
#merge 2 dictionary
my_dict.update(my_dict1)
print(my_dict)

