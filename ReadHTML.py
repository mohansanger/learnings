import pandas as pd

url="https://www.tutorialspoint.com/sql/sql-rename-table.htm"

table=pd.read_html(url, match="Field")

df = table[0]
print(df.head())