"""
Topic: Path Parameters and Query Parameters

FastAPI infers whether a function argument is a path param or a query
param based on whether it appears inside the route's path string.

Coming from Spring Boot, think of it this way:
- Path param   -> like @PathVariable
- Query param  -> like @RequestParam
- Type hints   -> replace the need for manual conversion/validation
                  (Spring does this via method signature types too,
                  but FastAPI generates the validation error responses
                  automatically, without you writing any code for it)

How to run this file:
    uvicorn theory.02_path_query_params:app --reload

Then open http://127.0.0.1:8000/docs to test interactively.
"""

from fastapi import FastAPI

app = FastAPI(
    title="Learning FastAPI",
    description="Path and query parameters example",
    version="0.1.0",
)

# --- Path parameters ---
# A path parameter is declared using curly braces in the route string,
# and MUST be provided as part of the URL (it's not optional).
@app.get("/users/{user_id}")
def read_user(user_id: int):
    """
    Example: GET /users/5 -> {"user_id": 5}

    Because user_id is typed as `int`, FastAPI automatically:
    - converts the string from the URL into an int
    - returns a 422 error if the value is not a valid int
      (e.g. GET /users/abc)
    This validation happens BEFORE your function body even runs.
    """
    return {"user_id": user_id}


# --- Query parameters ---
# Any function parameter that does NOT appear in the route path
# is treated as a query parameter. It's read from the URL after "?".
@app.get("/search")
def search_items(term: str, limit: int = 10):
    """
    Example: GET /search?term=laptop&limit=5
             -> {"term": "laptop", "limit": 5}

    - `term` has no default value, so it's REQUIRED.
      Calling GET /search without ?term=... returns a 422 error.
    - `limit` has a default value (10), so it's OPTIONAL.
      Calling GET /search?term=laptop uses limit=10 automatically.
    """
    return {"term": term, "limit": limit}


# --- Combining both ---
@app.get("/users/{user_id}/orders")
def read_user_orders(user_id: int, status: str = "all"):
    """
    Example: GET /users/5/orders?status=pending
             -> {"user_id": 5, "status": "pending"}

    user_id comes from the path (required, since it's in the route),
    status comes from the query string (optional, defaults to "all").
    """
    return {"user_id": user_id, "status": status}


# Key takeaways:
# 1. Path params: part of the URL structure, always required.
# 2. Query params: come after "?", required only if they have no default.
# 3. Type hints drive both the conversion AND the validation, for free.
# 4. Route order matters when routes could overlap
#    (e.g. "/users/count" must be declared BEFORE "/users/{user_id}",
#    otherwise "count" gets captured as user_id and fails int conversion).