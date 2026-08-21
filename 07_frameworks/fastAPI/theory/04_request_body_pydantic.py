"""
Topic: Request Body & Pydantic Models

So far, every endpoint received data via the URL (path/query params).
That's fine for simple GET requests, but for POST/PUT (creating or
updating a resource with complex data), you need a request BODY —
a JSON object sent in the request, not the URL.

Coming from Spring Boot, think of it this way:
- Pydantic BaseModel  -> like a DTO class, but validation rules live
                          directly on the fields (similar to combining
                          a DTO + Bean Validation annotations in one)
- @app.post(...)       -> like @PostMapping
- model as a parameter -> like @RequestBody automatically binding JSON
                          to your DTO class

How to run this file:
    uvicorn theory.04_request_body_pydantic:app --reload

Since request bodies aren't sent via URL, you can't test POST/PUT by
just typing a URL in the browser — use http://127.0.0.1:8000/docs
(Swagger lets you fill in the JSON body and send it) or a tool like
curl/HTTPie/Postman.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(
    title="Learning FastAPI",
    description="Request body and Pydantic models example",
    version="0.1.0",
)

# A Pydantic model describes the SHAPE of the data you expect to
# receive. Each attribute becomes a required field, unless it has a
# default value (making it optional, just like function parameters).
class ProductCreate(BaseModel):
    name: str
    price: float
    # Field(...) lets you add extra validation rules and metadata,
    # similar to @Min/@Max/@NotBlank annotations in Java.
    quantity: int = Field(default=0, ge=0)  # ge=0 -> "greater or equal to 0"

products: list[dict] = []

# When a parameter's type is a Pydantic model (not str/int/float/bool),
# FastAPI automatically knows to read it from the JSON request BODY,
# not from the URL. It also validates it before your function runs.
@app.post("/products")
def create_product(product: ProductCreate):
    """
    Example request body (sent as JSON, not in the URL):
        {
          "name": "Keyboard",
          "price": 250.0,
          "quantity": 5
        }

    If "price" is missing, or "quantity" is negative, FastAPI returns
    a 422 error automatically, listing exactly which fields failed —
    you never write that validation logic yourself.
    """
    new_product = product.model_dump()
    new_product["id"] = len(products) + 1
    products.append(new_product)
    return new_product

# You can combine a path param with a request body in the same endpoint.
class ProductUpdate(BaseModel):
    name: str | None = None
    price: float | None = None

@app.put("/products/{product_id}")
def update_product(product_id: int, updates: ProductUpdate):
    """
    Example: PUT /products/1
    Body: {"price": 199.99}

    Only fields actually provided in the body get updated — this
    pattern is common for partial updates (similar to PATCH semantics).
    `exclude_unset=True` tells Pydantic to only include fields the
    client actually sent, ignoring the ones left as default (None).
    """
    for existing in products:
        if existing["id"] == product_id:
            existing.update(updates.model_dump(exclude_unset=True))
            return existing

    raise HTTPException(status_code=404, detail="Product not found")

@app.get("/products")
def get_products():
    """
    Returns all products currently stored in memory.
    """
    return products

# Key takeaways:
# 1. Pydantic models = request body validation, similar to DTO + Bean
#    Validation, but declared directly as Python type hints.
# 2. FastAPI reads the body automatically when a parameter's type is a
#    BaseModel subclass — no annotation needed like @RequestBody.
# 3. `Field(...)` adds extra constraints (ge, le, min_length, etc).
# 4. `model_dump()` converts a Pydantic model back into a plain dict.
# 5. `exclude_unset=True` is the key trick for partial updates (PATCH-like
#    behavior even on a PUT endpoint).