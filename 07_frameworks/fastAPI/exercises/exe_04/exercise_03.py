"""
Exercise 3: Nested models + partial update

Goal:
    Combine everything: a nested Pydantic model (a model that contains
    another model as a field), full CRUD-style creation, and a partial
    update endpoint using exclude_unset.

Instructions:
    1. Create the FastAPI app instance.
    2. Define a Pydantic model `Address` with fields:
       - street: str
       - city: str
       - zip_code: str
    3. Define a Pydantic model `Customer` with fields:
       - name: str
       - email: str
       - address: Address (a NESTED model — the request body will have
         address as a nested JSON object)
    4. Define a Pydantic model `CustomerUpdate` with fields:
       - name: str | None = None
       - email: str | None = None
       (no address here — keep the update simple, address isn't
       updatable in this exercise)
    5. Create a module-level list called `customers` (starts empty).
    6. Create a POST "/customers" endpoint that:
       - receives a `Customer` in the request body
       - adds an "id" field (len(customers) + 1)
       - appends it to `customers` (use .model_dump() to store it as
         a plain dict)
       - returns the created dict
    7. Create a PATCH "/customers/{customer_id}" endpoint that:
       - receives a `CustomerUpdate` in the request body
       - finds the matching customer by id
       - raises HTTPException(404, "Customer not found") if missing
       - updates only the fields that were actually sent
         (use .model_dump(exclude_unset=True))
       - returns the updated customer dict

Run it with:
    uvicorn exercise_03:app --reload

Test in http://127.0.0.1:8000/docs:
    POST /customers
    Body: {
      "name": "Isaque",
      "email": "isaque@example.com",
      "address": {"street": "Main St", "city": "Franca", "zip_code": "14400-000"}
    }
    -> should work, returns id: 1

    PATCH /customers/1
    Body: {"email": "new_email@example.com"}
    -> should update ONLY the email, name and address stay the same

    PATCH /customers/999
    Body: {"email": "x@x.com"}
    -> should return 404
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# TODO: create the FastAPI app instance
app = FastAPI(
    title="Learning FastAPI: Exercise 3 - Nested models + partial update",
    description="""
      Combine everything: a nested Pydantic model (a model that contains
      another model as a field), full CRUD-style creation, and a partial
      update endpoint using exclude_unset.
         """,
    version="0.1.0",
)
# TODO: define the Address Pydantic model
# fields: street (str), city (str), zip_code (str)
class Address(BaseModel):
    street: str
    city: str
    zip_code: str

# TODO: define the Customer Pydantic model
# fields: name (str), email (str), address (Address)
class Customer(BaseModel):
    name: str
    email: str
    address: Address

# TODO: define the CustomerUpdate Pydantic model
# fields: name (str | None = None), email (str | None = None)
class CustomerUpdate(BaseModel):
    name: str | None = None
    email: str | None = None

# TODO: create the `customers` list (starts empty)
customers: list[dict] = []

# TODO: POST "/customers" endpoint receiving a Customer body
# add an "id" field, store as dict, append, and return it
@app.post("/customers")
def post_customers(customer: Customer):
    new_customer = customer.model_dump()
    new_customer["id"] = len(customers) + 1
    customers.append(new_customer)
    return new_customer

# TODO: PATCH "/customers/{customer_id}" endpoint receiving a
# CustomerUpdate body
# find the customer, raise 404 if missing, update only sent fields
@app.patch("/customers/{customer_id}")
def patch_customers(customer_id: int, updates: CustomerUpdate):
    for customer in customers:
        if customer["id"] == customer_id:
            customer.update(updates.model_dump(exclude_unset=True))
            return customer
    raise HTTPException(status_code=404, detail="Customer not found")
