import pandas as pd
import numpy as np

df=pd.DataFrame(np.random.rand(3,4),columns=list("ABCD"))
s=pd.Series(np.random.rand(10))
"""print(df)
print(df.dtypes)
print(df.index)
print(df.values)
print(df.shape)
print(df.columns)
print(df.ndim)
print(df.size)
print(df.empty)
print(s.head())
print(s.tail(3))
print(s.describe())
print(s.info())"""


df1=pd.DataFrame(np.random.rand(8,4),index=["a","b","c","d","e","f","g","h"],columns=["A","B","C","D"])
print(df1)
print(df1.loc[["a","d","g"],["B","C"]])