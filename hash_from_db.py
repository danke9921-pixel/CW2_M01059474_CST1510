import bcrypt

# Your user data as a list of dicts (could also come from a DB query)
users = [
    {"id": 1, "username": "Anna29", "password_hash": "$2b$12$OZmyDR0AQlecAq4INUXMlOoOyj1T/WGc9HzNBi4yZrp8iez0.Q7Bu", "role": "user"},
    {"id": 2, "username": "Ahmet", "password_hash": "$2b$12$mEYKNDmnWdZXxlqGZyFl/uDOYusGKFFwBUCG9osk.zkWXku.inz8K", "role": "user"},
    {"id": 3, "username": "Stevan200", "password_hash": "VolimCevapi~2", "role": "user"},
    {"id": 4, "username": "djanix1", "password_hash": "Mostar!1", "role": "user"},
    {"id": 5, "username": "Nahiyanatyourservice", "password_hash": "L0esife*P20", "role": "user"},
    {"id": 6, "username": "MrWasniowski", "password_hash": "LinDor*510", "role": "user"},
    {"id": 7, "username": "Navidherewegomdx", "password_hash": "Ap\"08s2_We", "role": "user"},
]

# Hash only the plain text ones
for user in users:
    pwd = user["password_hash"]
    if not pwd.startswith("$2b$"):  # already hashed passwords start with $2b$
        hashed = bcrypt.hashpw(pwd.encode("utf-8"), bcrypt.gensalt())
        user["password_hash"] = hashed.decode("utf-8")

# Preview the result
for user in users:
    print(user)