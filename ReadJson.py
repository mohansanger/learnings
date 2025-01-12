import pandas as pd
from io import StringIO

data= """[
   {"Name": "Braund", "Gender": "Male", "Age": 30},
   {"Name": "Cumings", "Gender": "Female", "Age": 25},
   {"Name": "Heikkinen", "Gender": "Female", "Age": 35}
]"""

stringObj=StringIO(data)
df=pd.read_json(stringObj)
print(df)