"""
Exercise 3: Custom exception + global exception handler

Goal:
    Go one level deeper than HTTPException: create your OWN exception
    class for a specific business rule, and register a global handler
    for it. This is closer to how larger FastAPI projects organize
    domain-specific errors (and is conceptually similar to a custom
    exception + @ExceptionHandler in Spring).

Instructions:
    1. Create the FastAPI app instance.
    2. Create a custom exception class `OutOfStockError(Exception)` that
       stores a `product_name: str` attribute in its __init__.
    3. Register a global handler using the @app.exception_handler
       decorator for OutOfStockError. It must return a JSONResponse with
       status_code=409 and content like:
       {"error": f"{product_name} is out of stock"}

       Reference signature (fill in the body):
       from fastapi.requests import Request
       from fastapi.responses import JSONResponse

       @app.exception_handler(OutOfStockError)
       def out_of_stock_handler(request: Request, exc: OutOfStockError):
           ...

    4. Create a module-level dict called `stock` mapping product names
       to available quantity, e.g. {"keyboard": 0, "mouse": 5}.
    5. Create a GET "/buy/{product_name}" endpoint that:
       - raises HTTPException(404, "Product not found") if the product
         name is not a key in `stock`
       - raises OutOfStockError(product_name) if stock[product_name] == 0
       - otherwise decreases stock[product_name] by 1 and returns
         {"bought": product_name, "remaining": stock[product_name]}

Run it with:
    uvicorn exercise_03:app --reload

Test in http://127.0.0.1:8000/docs:
    - GET /buy/keyboard -> 409, {"error": "keyboard is out of stock"}
    - GET /buy/mouse     -> works, remaining decreases each call
    - GET /buy/monitor   -> 404, {"detail": "Product not found"}
"""

from fastapi import FastAPI, HTTPException
from fastapi.requests import Request
from fastapi.responses import JSONResponse

# TODO: create the FastAPI app instance
app = FastAPI(
    title="Learning FastAPI: Exercise 3 - Custom exception + global exception handler",
    description='''
        Go one level deeper than HTTPException: create your OWN exception
    class for a specific business rule, and register a global handler
    for it. This is closer to how larger FastAPI projects organize
    domain-specific errors (and is conceptually similar to a custom
    exception + @ExceptionHandler in Spring).''',
    version="0.1.0"
)


# TODO: define the OutOfStockError custom exception class
# it should store `product_name` in its __init__
class OutOfStockError(Exception):
    def __init__(self, product_name: str):
        self.product_name = product_name
    
# TODO: register the global exception handler for OutOfStockError
# using @app.exception_handler(OutOfStockError)
@app.exception_handler(OutOfStockError)
def out_of_stock_handler(request: Request, exc: OutOfStockError):
    return JSONResponse(
        status_code=409,
        content={"error": f"{exc.product_name} is out of stock"}
    )

# TODO: create the `stock` dict with at least 2 products
stock = {
    "keyboard": 0,
    "mouse": 5
}

# TODO: GET "/buy/{product_name}" endpoint
# apply the checks described above, in order
@app.get("/buy/{product_name}")
def buy_product(product_name: str):
    if product_name not in stock:
        raise HTTPException(status_code=404, detail="Product not found")

    if stock[product_name] == 0:
        raise OutOfStockError(product_name)

    stock[product_name] -= 1

    return {
        "bought": product_name,
        "remaining": stock[product_name]
    }