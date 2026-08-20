"""
Exercise 2: Multiple error conditions, multiple status codes

Goal:
    Practice choosing the right status code for different kinds of
    problems in the same endpoint.

Instructions:
    1. Create the FastAPI app instance.
    2. Create a module-level list called `accounts` with at least 3
       dicts, each with "id" (int), "owner" (str), and "balance" (float).
    3. Create a GET "/accounts/{account_id}/withdraw" endpoint with a
       required query param `amount` (float) that:
       - raises HTTPException(400, "Amount must be positive")
         if amount <= 0
       - raises HTTPException(404, "Account not found")
         if no account matches account_id
       - raises HTTPException(400, "Insufficient funds")
         if amount > account balance
       - otherwise, subtracts amount from the account's balance and
         returns the updated account dict

    Think carefully about the ORDER of these checks — some validations
    should happen before you even try to find the account, others only
    make sense after you've found it.

Run it with:
    uvicorn exercise_02:app --reload

Test in http://127.0.0.1:8000/docs:
    - GET /accounts/1/withdraw?amount=-5     -> 400 Amount must be positive
    - GET /accounts/999/withdraw?amount=10   -> 404 Account not found
    - GET /accounts/1/withdraw?amount=999999 -> 400 Insufficient funds
    - GET /accounts/1/withdraw?amount=10     -> should work
"""

from fastapi import FastAPI, HTTPException

# TODO: create the FastAPI app instance
app = FastAPI(
    title="Learning FastAPI: Exercise 2 - Multiple error conditions, multiple status codes",
    description='''Practice choosing the right status code for different kinds of problems in the same endpoint.''',
    version="0.1.0"
)

# TODO: create the `accounts` list with at least 3 sample accounts
# each with "id", "owner", "balance"
accounts = [
    {"id": 1, "owner": "Alice", "balance": 1500.0},
    {"id": 2, "owner": "Bob", "balance": 3200.50},
    {"id": 3, "owner": "Carol", "balance": 750.25},
]

# TODO: GET "/accounts/{account_id}/withdraw" endpoint
# required query param: amount (float)
# apply the three validations described above, in a sensible order
@app.get("/accounts/{account_id}/withdraw")
def get_amount(account_id: int, amount: float):
    if amount <= 0:
        raise HTTPException (status_code=400, detail="Amount must be positive")
    temp = False
    index_account = None
    for account in accounts:
        if account["id"] == account_id:
            temp = True
            index_account = accounts.index(account)
            break
    if temp == False:
        raise HTTPException (status_code=404, detail="Account not found")
    if amount > accounts[index_account]["balance"]:
        raise HTTPException (status_code=400, detail="Insufficient funds")
    accounts[index_account]["balance"] -= amount
    return {"updated_account": accounts[index_account]}
    