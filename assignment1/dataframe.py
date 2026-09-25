import pandas as pd 
data = { 
    "Name": ["Anu", "Ravi", "Kiran", "Sita", "Rahul"], 
    "Age": [22, 25, 21, 24, 27], 
    "City": ["Rajahmundry", "Hyderabad", "Chennai", "Rajahmundry", "Hyderabad"], 
    "Salary": [25000, 45000, 30000, 35000, 55000], 
    "Department": ["IT", "HR", "IT", "Finance", "IT"] 
}
df = pd.DataFrame(data) 
print(df)

#filtering data
result = df[df["Salary"] > 30000] 
print(result) 

#or condation
result = df[
    (df["City"] == "Hyderabad") |
    (df["City"] == "chennai")
]
print(result)

#filter usin isin()
result = df[
    df["City"].isin(["Hyderabad", "Chennai"])
    ] 
print(result) 

#sort data ascending
df.sort_values("Salary")

#sort data deascending order
df.sort_values("Salary", ascending=False)

#BONUS
df["Bonus"] = df["Salary"] * 0.10 
print(df)

#TOTAL
df["TotalSalary"] = df["Salary"] + df["Bonus"] 
print(df) 

#NUMPY
import numpy as np 
df["Level"] = np.where( df["Salary"] >= 40000, "Senior", "Junior" ) 
print(df) 

import numpy as np 
df["Level"] = np.where( df["Age"] >= 22, "Senior", "Junior" ) 
print(df) 

#Groupby
result = df.groupby("Department")["Salary"].mean() 
print(result) 

result = df.groupby("Age")["Salary"].mean()
print(result)

#multiply agg
result = df.groupby("Department")["Salary"].agg( 
    ["count", "sum", "mean", "min", "max"] 
    ) 
print(result)

#groupby city
result = df.groupby("City")["Salary"].mean() 
print(result) 

#groupby city columns
result = df.groupby( ["City", "Department"] )["Salary"].mean() 
print(result)

#value counts
print(df["Department"].value_counts()) 

#city-wise
print(df["City"].value_counts()) 

#missing values
data = { 
    "Name": ["mahesh", "Ravi", "Kiran", "bhavani"], 
    "Age": [19, None, 21, 24], 
    "Salary": [25000, 45000, None, 35000] 
    } 
df = pd.DataFrame(data) 
print(df) 

#find miss values
print(df.isnull()) 
#count miss values
print(df.isnull().sum()) 
#find total values
print(df.isnull())

#Fill Age with average age 
df["Age"] = df["Age"].fillna(df["Age"].mean()) 

#Fill Salary with 0 
df["Salary"] = df["Salary"].fillna(0) 

#remove
df.dropna() 

#Remove Duplicate Data 
df.drop_duplicates() 
 
#For a particular 
df.drop_duplicates(subset=["Name"]) 

#renamecolumn
df.rename( columns={ 
    "Salary": "MonthlySalary", 
    "Age": "EmployeeAge" }, 
    inplace=True 
) 
print(df) 

#loc
print(df.loc[:, ["Name", "MonthlySalary"]])

result = df.loc[df["MonthlySalary"] > 30000]
print(result)
#real
data = { 
    "Employee": ["A", "B", "C", "D", "E", "F"], 
    "Department": ["IT", "HR", "IT", "Sales", "HR", "IT"], 
    "Salary": [40000, 30000, 50000, 35000, 32000, 60000], 
    "Experience": [2, 1, 4, 3, 2, 6] 
}
df = pd.DataFrame(data) 

