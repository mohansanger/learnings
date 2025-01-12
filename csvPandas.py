import pandas as pd

#pd.read_csv(r"C:\Users\Mohan.2.Singh\Downloads\Test PY\Book1.csv")

#creating a Data frame

df=pd.DataFrame([["Mss",33],["Kss",38]],columns=["Name","Age"])
df.to_csv(r"C:\Users\Mohan.2.Singh\Downloads\Test PY\Book1.csv")