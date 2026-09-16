import pandas as pd

df = pd.read_csv("ecommerce.csv.xls")

print(df.loc[df["Price"].idxmax()])
print(df.loc[df["Price"].idxmin()])
print(df["Rating"].mean())
print(df.groupby("Category")["Product"].count())
print((df["Price"] * df["Quantity"]).sum())