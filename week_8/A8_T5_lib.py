import hashlib

CREDENTIALS_FILE = "credentials.txt"
DELIMITER = ";"

def hash_password(PPassword: str) -> str:
    return hashlib.md5(PPassword.encode("UTF-8")).hexdigest()

def read_credentials() -> list[list[str]]:
    credentials: list[list[str]] = []
    with open(CREDENTIALS_FILE, "r", encoding="UTF-8") as source:
        for row in source:
            row = row.strip()
            if len(row) == 0:
                continue
            credentials.append(row.split(DELIMITER))
    return credentials
# print(readCredentials())

def register_user(PUsername: str, PPassword: str) -> None:
    new_user_id = len(read_credentials())
    row = DELIMITER.join([str(new_user_id), PUsername, hash_password(PPassword)])
    with open(CREDENTIALS_FILE, "a", encoding="UTF-8") as filehandle:
        filehandle.write(row + "\n")
    return None

def login_user(PUsername: str, PPassword: str):
    password_hashed = hash_password(PPassword)
    credentials = read_credentials()
    for user in credentials:
        username = user[1]
        stored_password = user[2]
        if username == PUsername and stored_password == password_hashed:
            return user
    return []

# additional
def exist_user(PUsername: str) -> bool:
    for user in read_credentials():
        if user[1] == PUsername:
            return True
    return False