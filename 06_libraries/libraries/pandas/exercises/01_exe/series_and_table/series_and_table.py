"""
Python Core - 06 Libraries (pandas)
Exercise 1: The Series and The Table (Easy - Fixation)
Folder: 01_series_and_table/
Main File: main.py

Rules:
1. Import 'pandas' as 'pd'.
2. Step A (Series):
   - Create a Pandas Series representing the inventory of 4 fruits. 
     Values: [15, 30, 12, 50]. 
     Index: ["Apples", "Bananas", "Cherries", "Dates"].
   - Print the Series.
3. Step B (DataFrame):
   - Create a DataFrame from a dictionary representing 3 books.
     Columns: "Title", "Author", "Pages".
     Row 1: "1984", "George Orwell", 328
     Row 2: "Dune", "Frank Herbert", 412
     Row 3: "Foundation", "Isaac Asimov", 255
   - Print the entire DataFrame.
4. Step C (Navigation):
   - Use '.iloc' to extract and print strictly the details of the second book ("Dune").
"""

#1
import pandas as pd
#2
fruits = pd.Series([15, 30, 12, 50], index=["Maçãs", "Bananas", "Cerejas", "Tâmaras"])
print(f"Fruits Series: \n{fruits}")
#3
print("")
data = {
    "Title":  ["1984", "Dune", "Foundation"],
    "Author": ["George Orwell", "Frank Herbert", "Isaac Asimov"],
    "Pages":  [328, 412, 255]
}
books = pd.DataFrame(data)
print(f"Books DataFrame: \n{books}")
#4
print("")
books.set_index("Title", inplace=True)
print(books.loc["Dune"])