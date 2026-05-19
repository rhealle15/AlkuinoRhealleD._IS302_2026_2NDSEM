def load_users(filename):
    users = {}

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            try:
                username, password = line.split(",")
                users[username.strip()] = password.strip()

            except ValueError:
                raise ValueError(
                    "Each line in users.txt must contain username,password"
                )

    return users


def main():
    try:
        users_RDA = load_users("users.txt")

    except FileNotFoundError:
        print("User credentials file not found.")
        return

    except ValueError as err:
        print("Error loading users:", err)
        return

    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if not username or not password:
        print("Username and password cannot be empty.")
        return

    if username in users_RDA and users_RDA[username] == password:
        print("Login successful!")

    else:
        print("Invalid username or password.")


if __name__ == "__main__":
    main()