import pandas as pd

data={
    "Name":["Ram", "Sita","Laxman","Bharat"],
    "Gender":["M","F","M","M"],
    "Age":["1B","2B","1M","1M"]
}

df=pd.DataFrame(data)
#print(df.index.dtype)

Series_data={"mss":1,"Dss":2,"Kss":3}
#s=pd.Series(Series_data,index=["mss","Dss","Kss","d"])
#print(s)

Series_data1=pd.Series(5,index=[0,1,2,3])
#print(Series_data1)

Series_data2=pd.Series([1,2,3,4,5],index=["a","b","c","d","e"])
#print(Series_data2(["a","b","c"]))


#DFrame={"mohan":31,"Deepika":31,"Kamal":38}
DFrame=[["mohan",31],["Deepika",31],["Kamal",38]]
DF=pd.DataFrame(DFrame,columns=["Name","Age"])
#print(DF)

