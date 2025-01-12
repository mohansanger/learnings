import pandas as pd
import numpy as np

url = 'https://raw.githubusercontent.com/pandas-dev/pandas/main/pandas/tests/io/data/csv/tips.csv'

df=pd.read_csv(url)
tips=df.head()
print(tips["total_bill"])


