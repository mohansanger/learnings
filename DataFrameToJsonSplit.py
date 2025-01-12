import pandas as pd
from json import loads,dumps

data1=pd.DataFrame([["x","y"],["z","w"]], index=["row-1","row-2"],columns=["Col-1","Col-2"])
result=data1.to_json(orient="table")
parsed=loads(result)
print(dumps(parsed,indent=4))

