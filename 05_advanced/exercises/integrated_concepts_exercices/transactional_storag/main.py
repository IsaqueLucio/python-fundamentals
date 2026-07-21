"""
Project 3: Transactional JSON Storage Engine
Folder: 03_transactional_storage/
Main File: main.py

Rules:
1. Create an initial file 'db.json' containing: {"balance": 1000, "user": "Isaque"}
2. Create a custom Context Manager class named 'AtomicTransaction':
   - '__init__(self, file_path)': Save the path.
   - '__enter__(self)': Open and load the JSON using 'json.load()'. Deep copy or save a backup of the original data in memory ('self.backup'). Return the loaded data dictionary so the user can modify it.
   - '__exit__(self, exc_type, exc_val, exc_tb)': 
     * If 'exc_type' is NOT None (meaning an exception occurred inside the 'with' block!), print f"[ROLLBACK] Error detected ({exc_val}). Canceling all changes!". Do NOT write to the disk. Return True to suppress the crash (or False if you want to see the traceback after rollback).
     * If 'exc_type' IS None (success!), use 'with open(..., "w")' and 'json.dump()' to overwrite 'db.json' with the modified data. Print "[COMMIT] Transaction saved successfully."

3. Test 1 (Success): Open 'AtomicTransaction', add 500 to "balance", let it finish, and verify 'db.json' is now 1500.
4. Test 2 (Rollback): Open 'AtomicTransaction', subtract 2000 from "balance". Check if balance < 0. If it is, explicitly 'raise ValueError("Insufficient funds!")'.
5. Verify that Test 2 triggered the rollback and 'db.json' remained at 1500!
"""

from pathlib import Path
from atomic_transaction import AtomicTransaction

db_path = Path(__file__).parent / "db.json"

with AtomicTransaction(db_path) as db:
  db["balance"] += 500

with AtomicTransaction(db_path) as db:
    db["balance"] -= 2000

    if db["balance"] < 0:
        raise ValueError("Insufficient funds!")

