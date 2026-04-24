correct_username_rda = "admin"
correct_password_rda = "1234"
attempts_rda = 0
while attempts_rda< 3:
    username_rda = input("Enter username: ")
    password_rda = input("Enter password: ")
    if username_rda == correct_username_rda and password_rda == correct_password_rda:
        print("Login Successful")
        break
    else:
        print("Invalid Credentials")
        attempts_rda += 1
if attempts_rda == 3:
    print("Account Locked")
