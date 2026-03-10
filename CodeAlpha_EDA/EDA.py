# ● Ask meaningful questions about the dataset before analysis.

# Price Related

# 1. What is the average laptop price?

# 2. What is the price distribution?

# 3. Are most laptops budget or premium?

# 4. Which laptop is most expensive?

# 5. Which is cheapest?

# Rating Related

# 1. What is the average rating?

# 2. Do higher-rated laptops cost more?

# 3. Which laptops have rating = 5?

# 4. Are low-rated laptops cheaper?

# Reviews Related

# 1. Do laptops with more reviews have higher ratings?

# 2. Is there a relationship between reviews and price?

# Pattern Questions

# 1. Which brand appears most frequently?

# 2. Which brand has highest average rating?

# 3. Which brand is most expensive on average?


#

import pandas as pd

df = pd.read_csv("laptops_dataset.csv")


# ● Explore the data structure, including variables and data types.

# 1. It shows the first 5 rows of your dataset.
print("First 5 Entries are follows\n", df.head(), "\n")

# 2. It is used to understand the structure of the dataset.
print("Structure of the Dataset is below\n", df.info(), "\n")

# 3. It is used to understand statistical summary of numerical columns.
print("Statistical summary of Numerical columns is below\n", df.describe(), "\n")

# 4. Data cleaning check

print(df.isnull().sum())
print(df.duplicated().sum())

print("Total Rows:", len(df))
print("Duplicate Rows:", df.duplicated().sum())

df.drop_duplicates(inplace=True)

print("Rows after removing duplicates:", len(df))

df.to_csv("laptops_dataset.csv", index=False)
print("File updated successfully ✅")

# ● Identify trends, patterns and anomalies within the data.

# 1. Price Distrubution
import matplotlib.pyplot as plt

plt.figure()
plt.hist(df["Price_INR"], bins=10)
plt.xlabel("Price (INR)")
plt.ylabel("Number of Laptops")
plt.title("Price Distribution")
plt.show()

# 2. Rating Distribution
plt.figure()
plt.hist(df["Rating"], bins=5)
plt.xlabel("Rating")
plt.ylabel("Count")
plt.title("Rating Distribution")
plt.show()

# 3. Reviews vs Rating

plt.figure()
plt.scatter(df["Reviews"], df["Rating"])
plt.xlabel("Number of Reviews")
plt.ylabel("Rating")
plt.title("Reviews vs Rating")
plt.show()

# 4. Price vs Rating

plt.figure()
plt.bar(df["Price_INR"].astype(str), df["Rating"])
plt.xlabel("Price (INR)")
plt.ylabel("Rating")
plt.title("Price vs Rating")
plt.show()


# ● Test hypotheses and validate assumptions using statistics and visualization.

print(df[["Price_INR", "Reviews", "Rating"]].corr())

print(df.groupby("Rating")["Price_INR"].mean()) # Hypothesis Testing


# ● Detect potential data issues or problems to address in further analysis.

# 1. Checking Outliers in Price
print(df[df["Price_INR"] > df["Price_INR"].mean() + 2*df["Price_INR"].std()])

# 2. Checking unusual Ratings
print(df[df["Rating"] == 0]) # Here, all are usual Ratings

# 3. Very high Reviews
print(df.sort_values(by="Reviews", ascending=False).head())


# ● Brand Analysis

df["Brand"] = df["Name"].str.split().str[0]

print(df["Brand"].value_counts())
print(df.groupby("Brand")["Price_INR"].mean().sort_values(ascending=False))
print(df.groupby("Brand")["Rating"].mean().sort_values(ascending=False))

# Creating Brand column and saving the updated dataset

df["Brand"] = df["Name"].str.split().str[0]
df.to_csv("laptops_dataset.csv", index=False)