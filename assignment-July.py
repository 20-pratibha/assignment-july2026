import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("supermarket_sales.csv")

print(df.head())
print(df.describe())
print(df.info())

# Compare total sales by branch
branch_sales = df.groupby("Branch")["Total"].sum().reindex(["A", "B", "C"])

print("\nTotal sales by branch:")
print(branch_sales)

plt.figure(figsize=(8, 5))
plt.bar(branch_sales.index, branch_sales.values, color=["#4C72B0", "#55A868", "#C44E52"])
plt.title("Total Sales by Branch")
plt.xlabel("Branch")
plt.ylabel("Total Sales")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("branch_total_sales.png", dpi=300)

# Bar chart of total sales by product line
product_line_sales = df.groupby("Product line")["Total"].sum().sort_values(ascending=False)

print("\nTotal sales by product line:")
print(product_line_sales)

plt.figure(figsize=(10, 6))
plt.bar(product_line_sales.index, product_line_sales.values, color="steelblue")
plt.title("Total Sales by Product Line")
plt.xlabel("Product Line")
plt.ylabel("Total Sales")
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("product_line_sales.png", dpi=300)

# Simple bar chart: average spending of Members vs Normal customers
customer_avg_spending = df.groupby("Customer type")["Total"].mean().reindex(["Member", "Normal"])

print("\nAverage spending by customer type:")
print(customer_avg_spending)

plt.figure(figsize=(6, 4))
plt.bar(customer_avg_spending.index, customer_avg_spending.values, color=["#4E79A7", "#F28E2B"])
plt.title("Average Spending: Members vs Normal")
plt.xlabel("Customer Type")
plt.ylabel("Average Total Spending")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("customer_avg_spending.png", dpi=300)

# Histogram of customer ratings to see the distribution
plt.figure(figsize=(8, 5))
plt.hist(df["Rating"], bins=10, color="mediumseagreen", edgecolor="black")
plt.title("Distribution of Customer Ratings")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("customer_ratings_histogram.png", dpi=300)
plt.show()





