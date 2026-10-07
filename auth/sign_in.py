from auth.auth import hash_password
from utils.storage import load


def signin():
    users = load("users.json", [])

    print("\n------------- SIGN IN -------------")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    for u in users:
        if u["username"].lower() == username.lower() and u["password"] == hash_password(password):
            print("\nLogin successful.")
            return {"username": u["username"], "role": u["role"]}

    print("\nInvalid username or password.")
    return None
