import pandas as pd
from io import BytesIO

df=pd.DataFrame([[1,2],[4,5]],index=["One","Two"],columns=["Rank","Sub"])

bio=BytesIO()

with pd.ExcelWriter(bio , engine="openpyxl") as writer:
  df.to_excel(writer,sheet_name="Sheet1")

bio.seek(0)
excelData=bio.read()
print(excelData)
  