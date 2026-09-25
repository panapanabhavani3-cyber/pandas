import pandas as pd

df = pd.read_csv("Weather.csv.xls")


print(df["Temperature"].mean())
print(df.loc[df["Temperature"].idxmax()])
print(df.loc[df["Temperature"].idxmin()])
print(df[df["Temperature"] > 35])
print(df.sort_values("Rainfall"))