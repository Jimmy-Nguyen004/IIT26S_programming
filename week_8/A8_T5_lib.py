import hashlib

CREDENTIALS_FILE = "credentials.txt"
DELIMITER = ";"

def hashPassword(PPassword: str) -> str:
    return hashlib.md5(PPassword.encode("UTF-8")).hexdigest()

def readCredentials() -> list[list[str]]:
    credentials: list[list[str]] = []
    with open(CREDENTIALS_FILE, "r", encoding="UTF-8") as source:
        for row in source:
            row = row.strip()
            if len(row) == 0:
                continue
            credentials.append(row.split(DELIMITER))
    return credentials
# print(readCredentials())

def registerUser(PUsername: str, PPassword: str) -> None:
    newUserID = len(readCredentials())
    row = DELIMITER.join([str(newUserID), PUsername, hashPassword(PPassword)])
    with open(CREDENTIALS_FILE, "a", encoding="UTF-8") as Filehandle:
        Filehandle.write(row + "\n")
    return None

def loginUser(PUsername: str, PPassword: str):
    passwordHash = hashPassword(PPassword)
    credentials = readCredentials()
    for user in credentials:
        username = user[1]
        stored_password = user[2]
        if username == PUsername and stored_password == passwordHash:
            return user
    return []

# additional
def existUser(PUsername: str) -> bool:
    for user in readCredentials():
        if user[1] == PUsername:
            return True
    return False