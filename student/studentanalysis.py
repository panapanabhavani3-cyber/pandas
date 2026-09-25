import pandas as pd
data = {
    "Name": ["Anu", "Ravi", "Sita", "Kiran", "Priya"],
    "Python": [85, 78, 92, 70, 88],
    "Pandas": [90, 75, 95, 68, 84],
    "Django": [80, 82, 89, 72, 91]
}

df = pd.DataFrame(data)

df["Total"] = df["Python"] + df["Pandas"] + df["Django"]
df["Average"] = df["Total"] / 3

print("Student Marks:")
print(df)

print("\nHighest Marks:")
print(df.loc[df["Total"].idxmax()])