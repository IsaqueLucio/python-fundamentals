"""
Exercise 1: Basic Pydantic model for POST

Goal:
    Practice defining a Pydantic model and using it as a request body.

Instructions:z
    1. Create the FastAPI app instance.
    2. Define a Pydantic model `Contact` with fields:
       - name: str (required)
       - email: str (required)
       - phone: str | None = None (optional)
    3. Create a module-level list called `contacts` (starts empty).
    4. Create a POST "/contacts" endpoint that:
       - receives a `Contact` in the request body
       - creates a dict from it with an added "id" (len(contacts) + 1)
       - appends it to `contacts`
       - returns the created dict

Run it with:
    uvicorn exercise_01:app --reload

Test in http://127.0.0.1:8000/docs (use the "Try it out" button, since
this is a POST request and can't be tested by just typing a URL):
    POST /contacts
    Body: {"name": "Isaque", "email": "isaque@example.com"}
    -> should return the contact with "id": 1 and "phone": null

    POST /contacts
    Body: {"name": "Isaque"}
    -> should return a 422 error (email is required)
"""

from fastapi import FastAPI
from pydantic import BaseModel

# TODO: create the FastAPI app instance
app = FastAPI(
    title="Learning FastAPI: Exercise 1 - Basic Pydantic model for POST",
    description="Practice defining a Pydantic model and using it as a request body.",
    version="0.1.0",
)

# TODO: define the Contact Pydantic model
# fields: name (str), email (str), phone (str | None = None)
class Contact(BaseModel):
    name: str
    email: str
    phone: str | None = None

# TODO: create the `contacts` list (starts empty)
contacts: list[dict] = []

# TODO: POST "/contacts" endpoint receiving a Contact body
# add an "id" field and append it to `contacts`, then return it
@app.post("/contacts")
def post_contact(contact: Contact):
    new_contact = contact.model_dump()
    new_contact["id"] = len(contacts) + 1
    contacts.append(new_contact)
    return new_contact

