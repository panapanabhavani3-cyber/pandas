import pandas as pd

# Read CSV file
df = pd.read_csv("sales.csv")

print("Sales Data:")
print(df)

# Calculate Total Sales
df["Total Sales"] = df["Quantity"] * df["Price"]

print("\nTotal Sales:")
print(df[["Product", "Total Sales"]])

# Calculate Total Revenue
total_revenue = df["Total Sales"].sum()

print("\nTotal Revenue:")
print(total_revenue)

# Find Highest Selling Product
highest = df.loc[df["Total Sales"].idxmax()]

print("\nHighest Selling Product:")
print(highest["Product"])
print("Sales:", highest["Total Sales"])

# Save final result
df.to_csv("final_sales_result.csv", index=False)

print("\nFinal sales result saved successfully!")