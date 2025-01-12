import pandas as pd

df=pd.DataFrame({"Name":["Braund", "Cumings", "Heikkinen"], 
"Gender": ["Male", "Female", "Female"],
"Age": [30, 25, 25]})

#print(df)

#If json file doesn't exist then it will create new json file 

path=r"C:\Users\Mohan.2.Singh\Downloads\Test PY\pandas.json"
df.to_json(path,orient="records",lines=True)