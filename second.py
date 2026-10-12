credential = {"username": "Jimmy", "password": "ABCD"}
for value, correct in credential.items():
    for _ in range(3):
        if input(f"{value}: ") == correct:
            break
        print(f"Invalid username.")
    else:
        print("No more chances.")
        break
else:
    print("Login succesful!")
print("Exiting program.")