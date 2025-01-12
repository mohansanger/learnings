my_Tuple=("Coforge", "Accenture", "LNT")

print("Coforge" in my_Tuple)
print("NTT" not in my_Tuple)

for items in my_Tuple:
 print(items,end="\n")

#my_Tuple[0]="Gen"
#print(my_Tuple)
#del my_Tuple
#print(my_Tuple)

new_element="NTT-Data"
#convert Tuple to list
my_Tuple1=list(my_Tuple)
def modifyTuple(my_Tuple1,new_element):
    my_Tuple1.append(new_element)
    my_Tuple=tuple(my_Tuple1)
    return my_Tuple

print(modifyTuple(my_Tuple1,new_element))

messg="""This is mohan singh
i am a software developer in python 
do you wanna hear more about"""
#messg=messg.upper()
#print(messg)
#messg=messg.partition
#print(messg)

#f=messg.index("is")
#print(f)
f=messg.find("mohan")
print(f)