import pandas as pd

url=r"C:\Users\Mohan.2.Singh\Downloads\Test PY\Excel.xlsx"
url1=r"C:\Users\Mohan.2.Singh\Downloads\Test PY\Write_Excel1.xlsx"
url2=r"C:\Users\Mohan.2.Singh\Downloads\Test PY\Multiple_Excel1.xlsx"
#df=pd.read_excel(url,sheet_name="Info")
#df=pd.read_excel(url)#,sheet_name="Info")
#df=pd.read_excel(url,sheet_name=[0,1])
#print(df)
#df.to_excel(url1)


df=pd.DataFrame([[1,2],[4,5]],index=["One","Two"],columns=["Rank","Sub"])
df1=pd.DataFrame([[10,20],[40,53]],index=["Three","Four"],columns=["Rank1","Sub1"])
#df.to_excel(url1)

with pd.ExcelWriter(url2,mode="a") as writer:
  df.to_excel(writer,sheet_name="S3")
  df1.to_excel(writer,sheet_name="S4")