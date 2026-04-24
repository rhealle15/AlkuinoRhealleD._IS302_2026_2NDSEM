def register_rda():
    username_rda = input("Enter username: ")
    password_rda = input("Enter password: ")
    with open("users.txt", "a") as file_rda:
        file_rda.write(username_rda + "," + password_rda + "\n")
    print("Registration successful!")

def login_rda():
    username_rda = input("Enter username: ")
    password_rda = input("Enter password: ")
    try:
        with open("users.txt", "r") as file_rda:
            for line_rda in file_rda:
                stored_user_rda, stored_pass_rda = line_rda.strip().split(",")
                if username_rda == stored_user_rda and password_rda == stored_pass_rda:
                    print("Login successful!")
                    return
        print("Invalid credentials!")
    except FileNotFoundError:
        print("No users registered yet!")

def main_rda():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice_rda = input("Enter choice: ")
        
        if choice_rda == "1":
            register_rda()
        elif choice_rda == "2":
            login_rda()
        elif choice_rda == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

main_rda()