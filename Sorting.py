import pandas as pd
import numpy as np
#Lable by Sorting
"""unsorted_df=pd.DataFrame(np.random.rand(10,2), index=[1,4,6,3,8,7,2,9,5,0],columns=["Col-1","Col-2"])
sorted_df=unsorted_df.sort_index(ascending=False)
print(sorted_df)"""

"""unsorted_df=pd.DataFrame(np.random.rand(6,4),index=[5,4,3,2,6,1],columns=["A","B","C","D"])
print(unsorted_df.sort_index())
sorted_df=unsorted_df.sort_index(axis=1)
print(sorted_df)"""

"""pandas_series=pd.Series([10,11,12,5,50,4])
print(pandas_series)
print(pandas_series.sort_values(ascending=True))"""

df=pd.DataFrame({"Col-1":[1,2,3,4],"Col-2":[5,6,3,2],"Col-3":[3,0,2,1]})
print(df)

#print(df.sort_values(by=["Col-2","Col-3"]))

"""s=pd.Series(np.random.rand(3),index=["a","b","c"])
print(s)
print(s.reindex(["d","e","f"]))"""
for key,value in df.items():
    print(key,value)






