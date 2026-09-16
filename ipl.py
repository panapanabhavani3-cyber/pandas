import pandas as pd

df = pd.read_csv("IPL.csv.xls")

print(df["Runs"].max())
print(df.sort_values("Runs", ascending=False).head(5))
print(df.groupby("Team")["Average"].mean())
print(df["Strike Rate"].max())
print(df.sort_values("Runs", ascending=False))