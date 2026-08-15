"""
Python Core - 06 Libraries (pandas)
Exercise 2: The Index Navigator (Intermediate - Logic & Interpretation)
Folder: 02_index_navigator/
Main File: main.py

Rules:
1. Import 'pandas' as 'pd'.
2. Create a DataFrame containing data for 4 tech stocks:
   - "Ticker": ["AAPL", "MSFT", "GOOGL", "AMZN"]
   - "Price": [175.50, 310.20, 135.40, 130.00]
   - "Sector": ["Hardware", "Software", "Web", "E-commerce"]
3. Step A (Setting the Index):
   - By default, Pandas assigns a numeric index (0, 1, 2, 3).
   - Update the DataFrame so that the "Ticker" column becomes the permanent index using '.set_index()'.
   - Print the updated DataFrame to verify the index changed.
4. Step B (Label Navigation with .loc):
   - Use '.loc' to extract and print the exact "Price" of the "MSFT" stock.
   - Use '.loc' to extract and print all details (Price and Sector) for the "GOOGL" stock.
"""
#1
import pandas as pd
#2
print("")
data = {
   "Ticker": ["AAPL", "MSFT", "GOOGL", "AMZN"],
   "Price": [175.50, 310.20, 135.40, 130.00],
   "Sector": ["Hardware", "Software", "Web", "E-commerce"]
}
tech_stocks = pd.DataFrame(data)
print(f"Pure Tech Stocks: \n{tech_stocks}")
#3
print("")
tech_stocks.set_index("Ticker", inplace=True)
print(f"Tech Stocks with ticket index: \n{tech_stocks}")
#4
print("")
print(f"Stock MSFT price: ${tech_stocks.loc["MSFT"]["Price"]}\n")
print(f"Stock GOOGL:\n {tech_stocks.loc["GOOGL"]}")

