"""
Exercise 1: Basic path parameters

Goal:
    Practice reading a single path parameter and using its type hint
    for automatic validation.

Instructions:
    1. Create the FastAPI app instance.
    2. Create a GET "/products/{product_id}" endpoint where product_id
       is an int. Return a dict like {"product_id": product_id}.
    3. Create a GET "/products/{product_id}/reviews/{review_id}" endpoint
       with TWO path params, both ints. Return a dict with both values.

Run it with:
    uvicorn exercise_01:app --reload

Test in http://127.0.0.1:8000/docs:
    - GET /products/10          -> should work
    - GET /products/abc         -> should return a 422 validation error
    - GET /products/10/reviews/3 -> should work
"""

from fastapi import FastAPI

# TODO: create the FastAPI app instance
app = FastAPI(
    title="Learning FastAPI: Exercise 1 - Basic path parameters",
    description="Practice reading a single path parameter and using its type hint for automatic validation.",
    version="0.1.0",
)

# TODO: GET "/products/{product_id}" endpoint (product_id: int)
@app.get("/products/{product_id}")
def get_products(product_id: int):
    '''
    Return the product by ID.
    '''
    return {
        "product_id": product_id
        }

# TODO: GET "/products/{product_id}/reviews/{review_id}" endpoint
# (both product_id and review_id: int)
@app.get("/products/{product_id}/reviews/{review_id}")
def get_product_reviw(product_id: int, review_id: int):
    '''
    Return the review by the ID of both product and review.
    '''
    return {
        "product_id": product_id,
        "review_id": review_id
    }