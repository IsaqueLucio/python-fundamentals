"""
Python Core - 06 Libraries (pandas)
Exercise 9: The E-commerce Aggregation Engine (Hard - Problem Solving)
Folder: 09_ecommerce_aggregation/
Main File: main.py

Scenario:
You are building an analytics dashboard for an e-commerce API. You have a table of products and a table of sales. You need to join them and generate a complex report showing total revenue, average order value, and total units sold per product category.

Rules:
1. Import 'pandas' as 'pd'.
2. Create the DataFrames:
   products = pd.DataFrame({
       "ProductID": ["P1", "P2", "P3", "P4"],
       "Category": ["Electronics", "Electronics", "Furniture", "Books"],
       "Price": [800.0, 50.0, 120.0, 15.0]
   })
   
   sales = pd.DataFrame({
       "SaleID": [1, 2, 3, 4, 5],
       "ProductID": ["P1", "P1", "P3", "P2", "P1"],
       "Quantity_Sold": [2, 1, 4, 10, 1]
   })
3. Step A (Merge):
   - Perform an INNER JOIN to combine 'products' and 'sales' on "ProductID". Save it as 'merged_data'.
4. Step B (Derived Column):
   - Create a new column in 'merged_data' called "Total_Revenue". 
   - Formula: "Price" * "Quantity_Sold".
5. Step C (Complex Aggregation):
   - Group the 'merged_data' by "Category".
   - Use the '.agg()' method to calculate three metrics simultaneously:
     * The SUM of "Total_Revenue" (Total money made per category)
     * The SUM of "Quantity_Sold" (Total items sold per category)
     * The COUNT of "SaleID" (Number of transactions per category)
   - Print this final executive report.
"""
#1
import pandas as pd
#2
print("")
products = pd.DataFrame({
   "ProductID": ["P1", "P2", "P3", "P4"],
   "Category": ["Electronics", "Electronics", "Furniture", "Books"],
   "Price": [800.0, 50.0, 120.0, 15.0]
})   
sales = pd.DataFrame({
   "SaleID": [1, 2, 3, 4, 5],
   "ProductID": ["P1", "P1", "P3", "P2", "P1"],
   "Quantity_Sold": [2, 1, 4, 10, 1]
})
print(f"Products: \n{products}\n")
print(f"Sales: \n{sales}")
#3
print("")
merged_data = pd.merge(products, sales, on="ProductID", how="inner")
print(f"Merged Data: \n{merged_data}")
#4
print("")
merged_data["Total_Revenue"] = merged_data["Price"] * merged_data["Quantity_Sold"]
print(f"Merged Data with the new column 'Total_Revenue': \n{merged_data}")
#5
print("")
final_executive_report = merged_data.groupby("Category").agg({
    "Total_Revenue": ["sum"],
    "Quantity_Sold": ["sum"],
    "SaleID": ["count"]
})
print(f"Final executive report: \n{final_executive_report}")