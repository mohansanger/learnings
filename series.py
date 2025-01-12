import pandas as pd

"""data=pd.Series(["a","b","c","d"])
#print(data[:3])
print(data[-3:])
print(data[:-3])
print(data[0:2])"""

data=pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
#print(data)
#data['a':'b']=[10,20]
#print(data)
#print(data+2)
#print(data-2)
#print(data%2)
print(data.to_frame(name="Number"))
print(repr(data.to_string()))


