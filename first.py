valid_username = "Jimmy"
valid_password = "ABCD"
max_attempts = 3

count_username = 0
while count_username < max_attempts:
    username = input("Username: ")
    if username == valid_username:
        break
    count_username += 1
    print("Invalid username!")

if count_username == max_attempts:
    print("No more chances.")
else:
    count_password = 0
    while count_password < max_attempts:
        password = input("Password: ")
        if password == valid_password:
            print("Login successful.")
            break
        count_password += 1
        print("Invalid password!")

    if count_password == max_attempts:
        print("No more chances.")

print("Exiting program.")
