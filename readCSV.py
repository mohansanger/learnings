import pandas as pd

from io import StringIO

data=data = """Name,Gender,Age
Braund,male,22
Cumings,female,38
Heikkinen,female,26
Futrelle,female,35"""

#obj=StringIO(data)

#df=pd.read_csv(obj)
#print(df)

url=r"C:\Users\Mohan.2.Singh\Downloads\Test PY\pandas.csv"
#df1=pd.read_table(url,sep=',')
#print(df1.head(2))

d=d = {'Car': ['BMW', 'Lexus', 'Audi', 'Mercedes', 'Jaguar', 'Bentley'],
'Date_of_purchase': ['2024-10-10', '2024-10-12', '2024-10-17', '2024-10-16', '2024-10-19', '2024-10-22']}

df=pd.DataFrame(d)
df.to_csv(url)