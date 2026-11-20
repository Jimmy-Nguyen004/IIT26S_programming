import template as temp
import A8_T5_lib as lib

def showMainOptions() -> None:
    print("Options:\n1 - Login\n2 - Register\n0 - Exit")
    return None

def showUserOptions() -> None:
    print("User menu:\n1 - View profile\n2 - Change password\n0 - Log out")

def userMenu(PUser: list[str]) -> None:
    while True:
        showUserOptions()
        choice = temp.askChoice()
        if choice == 1:
            print("Profile ID {} - {}".format(PUser[0], PUser[1]))
        elif choice == 2:
            print("Feature not implemented.")
        elif choice == 0:
            print("Logging out...")
            print()
            break
        else:
            print("Unknown option!")
        print()
    return None

def main() -> None:
    print("Program starting.")
    while True:
        showMainOptions()
        choice = temp.askChoice()
        if choice == 1:
            username = input("Insert username: ")
            password = input("Insert password: ")
            user = lib.loginUser(username, password)
            if len(user) == 0:
                print("Authentication failed!")
            else:
                print("Authentication successful!")
                print()
                userMenu(user)
                continue

        elif choice == 2:
            username = input("Insert username: ")
            if lib.existUser(username):
                print("Username already taken!")
            else:
                password = input("Insert password: ")
                lib.registerUser(username, password)
                print("User registration completed!")

        elif choice == 0:
            print("Exiting program.")
            print()
            break

        else:
            print("Unknown option!")
        print()
    return None

if __name__ == "__main__":
    main()