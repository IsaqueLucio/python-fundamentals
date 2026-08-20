"""
Exercise 1: Basic HTTPException

Goal:
    Rewrite a "manual JSONResponse" pattern using the idiomatic
    HTTPException instead.

Instructions:
    1. Create the FastAPI app instance.
    2. Create a module-level list called `users` with at least 3 dicts,
       each with "id" (int) and "username" (str).
    3. Create a GET "/users/{user_id}" endpoint that:
       - returns the matching user if found
       - raises HTTPException(status_code=404, detail="User not found")
         if no user matches

Run it with:
    uvicorn exercise_01:app --reload

Test in http://127.0.0.1:8000/docs:
    - GET /users/1    -> should work
    - GET /users/999  -> should return 404 with {"detail": "User not found"}
"""

from fastapi import FastAPI, HTTPException

# TODO: create the FastAPI app instance
app = FastAPI(
    title="Learning FastAPI: Exercise 1 - Basic HTTPException",
    description='''Rewrite a "manual JSONResponse" pattern using the idiomatic HTTPException instead.''',
    version="0.1.0",
)

# TODO: create the `users` list with at least 3 sample users
# each with "id" and "username"
users = [
    {"id": 1, "username": "alice"},
    {"id": 2, "username": "bob"},
    {"id": 3, "username": "carol"},
]

# TODO: GET "/users/{user_id}" endpoint (user_id: int)
# raise HTTPException(status_code=404, detail="User not found") if missing
@app.get("/users/{user_id}")
def get_users(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")