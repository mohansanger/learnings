list=[1,2,2,3,3,4,4,2,2,6,7,6,6]
newList=[]
for i in list:
    if i not in newList:
        newList.append(i)
print(list)
print(newList)

