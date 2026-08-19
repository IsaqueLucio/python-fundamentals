"""
Exercise 2: Required vs optional query parameters

Goal:
    Practice the difference between a required query param (no default
    value) and an optional one (has a default value).

Instructions:
    1. Create the FastAPI app instance.
    2. Create a GET "/books" endpoint with:
       - a required query param `author` (str)
       - an optional query param `year` (int), defaulting to None
       Return a dict with both values, e.g.
       {"author": author, "year": year}.
    3. Create a GET "/products" endpoint with:
       - an optional query param `min_price` (float), default 0.0
       - an optional query param `max_price` (float), default 1000.0
       - an optional query param `in_stock` (bool), default True
       Return a dict with all three values.

Run it with:
    uvicorn exercise_2:app --reload

Test in http://127.0.0.1:8000/docs:
    - GET /books?author=Tolkien          -> should work, year is null
    - GET /books                          -> should return a 422 error
    - GET /products?min_price=50&in_stock=false -> should work
"""

from fastapi import FastAPI

# TODO: create the FastAPI app instance
app = FastAPI(
    title="Learning FastAPI: Exercise 2 - Required vs optional query parameters",
    description="Practice the difference between a required query param (no default value) and an optional one (has a default value).",
    version="0.1.0",
)

# TODO: GET "/books" endpoint
# required: author (str)
# optional: year (int, default None)
@app.get("/books")
def get_book(author: str, year: int = None):
    '''
    Return book by author and year.
    '''
    return {
        "author": author,
        "year": year
    }

# TODO: GET "/products" endpoint
# optional: min_price (float, default 0.0)
# optional: max_price (float, default 1000.0)
# optional: in_stock (bool, default True)
@app.get("/products")
def get_products(min_price: float = 0.0, 
                 max_price: float = 1000.00, 
                 in_stock: bool = True):
    '''
    Product filter by minimum and maximum price and by stock status. 
    '''
    return {
        "min_price": min_price,
        "max_price": max_price,
        "in_stock": in_stock
    }