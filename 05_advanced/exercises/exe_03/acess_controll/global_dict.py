CURRENT_USER = {"username": "Mike", "role": "guest"}

def change_role(new_role: str):
    CURRENT_USER["role"] = new_role