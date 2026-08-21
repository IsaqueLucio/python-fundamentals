"""
Exercise 1: Hiding a sensitive field with response_model

Goal:
    Practice the core use case of response_model: preventing an
    internal-only field from leaking into the API response.

Instructions:
    1. Create the FastAPI app instance.
    2. Define a Pydantic model `AccountCreate` (input) with fields:
       - owner: str
       - pin: str  (a sensitive 4-digit PIN, should NEVER be returned)
    3. Define a Pydantic model `AccountOut` (output) with fields:
       - id: int
       - owner: str
       (notice: no `pin` field here)
    4. Create a module-level list called `accounts` (starts empty).
    5. Create a POST "/accounts" endpoint with response_model=AccountOut
       that:
       - receives an AccountCreate in the body
       - builds a dict with "id", "owner", AND "pin" (store the full
         thing internally, including the pin)
       - appends it to `accounts`
       - returns the full dict (response_model will strip "pin" out
         automatically — you don't need to remove it yourself)

Run it with:
    uvicorn exercise_01:app --reload

Test in http://127.0.0.1:8000/docs:
    POST /accounts
    Body: {"owner": "Isaque", "pin": "1234"}
    -> response should have "id" and "owner" ONLY, no "pin" field
"""

from fastapi import FastAPI
from pydantic import BaseModel

# TODO: create the FastAPI app instance
app = FastAPI(
    title="Learning FastAPI: Exercise 1 - Hiding a sensitive field with response_model",
    description="Practice the core use case of response_model: preventing an internal-only field from leaking into the API response.",
    version="0.1.0",
)

# TODO: define AccountCreate (input model)
# fields: owner (str), pin (str)
class AccountCreate(BaseModel):
    owner: str
    pin: str

# TODO: define AccountOut (output model)
# fields: id (int), owner (str) -- no pin!
class AccountOut(BaseModel):
    id: int
    owner: str

# TODO: create the `accounts` list (starts empty)
accounts: list[dict] = []

# TODO: POST "/accounts" endpoint with response_model=AccountOut
# store the full dict (with pin) internally, return it anyway --
# response_model takes care of filtering it out
@app.post("/accounts", response_model=AccountOut)
def post_accounts(account: AccountCreate):
    new_account = {
        "id": len(accounts) + 1,
        "owner": account.owner,
        "pin": account.pin
    }
    accounts.append(new_account)
    return new_account
