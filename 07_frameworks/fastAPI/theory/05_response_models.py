"""
Topic: Response Models

So far, every endpoint returns whatever dict/model we build by hand.
That works, but it has a problem: if your internal data has sensitive
or irrelevant fields (like a password hash, or internal flags), you
might accidentally leak them in the API response.

`response_model` lets you declare exactly what SHAPE the response
must have — FastAPI will filter/validate the output against it,
regardless of what your function actually returns internally.

Coming from Spring Boot, think of it this way:
- Input Pydantic model (Exercise 4)  -> like a request DTO
- Output Pydantic model (this topic) -> like a response DTO
- Having TWO separate models (input vs output) is normal and expected,
  the same way you wouldn't reuse a JPA @Entity directly as a
  @RequestBody/@ResponseBody in a well-designed Spring API.

How to run this file:
    uvicorn theory.05_response_models:app --reload
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Learning FastAPI",
    description="Response models example",
    version="0.1.0",
)


# --- The problem response_model solves ---
# Imagine our internal user data includes a hashed password. If we
# just return the dict/model directly, we might leak it by accident.
class UserCreate(BaseModel):
    username: str
    email: str
    password: str  # plain password, only used for input


class UserOut(BaseModel):
    """
    This is the OUTPUT shape: notice there's no `password` field here.
    Even if our internal object has a password field, FastAPI will
    strip it out because it's not declared in UserOut.
    """
    id: int
    username: str
    email: str


users_db: list[dict] = []


# `response_model=UserOut` tells FastAPI: "no matter what this function
# returns, filter/validate it against UserOut before sending it out."
@app.post("/users", response_model=UserOut)
def create_user(user: UserCreate):
    # In a real app you'd hash the password before storing it.
    new_user = {
        "id": len(users_db) + 1,
        "username": user.username,
        "email": user.email,
        "password": user.password,  # stored internally...
    }
    users_db.append(new_user)

    # ...but even though we return the FULL dict (including password),
    # response_model=UserOut strips it from the actual JSON response.
    return new_user


@app.get("/users/{user_id}", response_model=UserOut)
def get_user(user_id: int):
    for user in users_db:
        if user["id"] == user_id:
            return user  # password still gets stripped automatically
    return {}


# --- response_model with lists ---
# To return a list of a model, use list[Model] as the response_model.
@app.get("/users", response_model=list[UserOut])
def list_users():
    return users_db


# Key takeaways:
# 1. response_model defines what the CLIENT sees, independent of what
#    your function internally works with.
# 2. It's common (and good practice) to have separate Input and Output
#    models, even if they look similar — this avoids leaking sensitive
#    or internal-only fields by accident.
# 3. response_model also shows up in the auto-generated /docs, so the
#    API consumer knows exactly what shape to expect back.
# 4. For endpoints returning a list, use response_model=list[YourModel].