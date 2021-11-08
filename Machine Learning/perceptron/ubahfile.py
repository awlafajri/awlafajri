import pandas as pd

df=pd.read_table("datamainan.txt")
print(df.head(5))
print(df.columns)

df.to_csv("datamainanrev.csv",index=False)