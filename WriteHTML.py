import pandas as pd

df=pd.DataFrame([[2,3],[4,5]], columns=["A","B"], index=["MSS","DSS"])

print(df.to_html())
