"""
Topic: Error Handling with HTTPException

In exercise 3 of the previous topic, you used JSONResponse to return a
custom status code manually. That works, but FastAPI has an idiomatic,
purpose-built way to do this: raising HTTPException.

Coming from Spring Boot, think of it this way:
- HTTPException           -> like throwing a ResponseStatusException
- raise HTTPException(...) -> stops execution immediately (like a Java
                               exception), FastAPI catches it and builds
                               the JSON error response for you
- @app.exception_handler   -> like a @ExceptionHandler / @ControllerAdvice,
                               for handling custom exception types globally

How to run this file:
    uvicorn theory.03_error_handling:app --reload
"""

from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="Learning FastAPI",
    description="Error handling with HTTPException",
    version="0.1.0",
)

# Simulating a "database" again, like in the previous topics.
products = [
    {"id": 1, "name": "Keyboard", "price": 250.0},
    {"id": 2, "name": "Mouse", "price": 90.0},
]


# --- The manual way (what you already did with JSONResponse) ---
# This works, but you have to remember to build the response yourself
# every single time, and it doesn't stop execution automatically.
@app.get("/products-manual/{product_id}")
def get_product_manual(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product

    from fastapi.responses import JSONResponse
    return JSONResponse(
        status_code=404,
        content={"error": "Product not found"},
    )


# --- The idiomatic way: raising HTTPException ---
# `raise` immediately stops the function. FastAPI catches HTTPException
# and automatically converts it into a proper JSON error response,
# in the format: {"detail": "<your message>"}.
@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product

    # No need to import JSONResponse, no need to remember the exact
    # response shape. FastAPI handles the "plumbing" for you.
    raise HTTPException(status_code=404, detail="Product not found")


# --- Using different status codes for different problems ---
@app.post("/products")
def create_product(name: str, price: float):
    if price <= 0:
        # 400 Bad Request: the client sent invalid data
        raise HTTPException(status_code=400, detail="Price must be positive")

    for product in products:
        if product["name"] == name:
            # 409 Conflict: the resource already exists
            raise HTTPException(status_code=409, detail="Product already exists")

    new_product = {
        "id": len(products) + 1, 
        "name": name, 
        "price": price
        }
    products.append(new_product)
    return new_product


# Key takeaways:
# 1. `raise HTTPException(status_code=..., detail=...)` is the standard,
#    idiomatic way to return errors in FastAPI — prefer it over building
#    a JSONResponse by hand.
# 2. Common status codes to know:
#    400 Bad Request    -> client sent invalid/malformed data
#    401 Unauthorized    -> missing/invalid authentication
#    403 Forbidden        -> authenticated, but not allowed
#    404 Not Found         -> resource doesn't exist
#    409 Conflict           -> request conflicts with current state
#    422 Unprocessable Entity -> FastAPI raises this AUTOMATICALLY when
#                                 type validation fails (you don't write
#                                 this one yourself)
# 3. Because `raise` stops execution immediately, you don't need `else`
#    or early `return` gymnastics — the function just ends there.