import pandas as pd

df = pd.read_csv("Bank.csv.xls")

print(df["Balance "].max())
print(df["Balance "].min())
print(df[df["Loan "] > 500000])
print(df.groupby("City")["Name"].count())
print(df["Balance "].sum())