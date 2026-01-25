# mini task: password login system

password = "admin123"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    user_input = input("Enter the password: ")

    if user_input == password:
        print("Login successful")
        break
    else:
        attempts += 1
        print("Incorrect password")
        print("Attempts left:",max_attempts - attempts)

if attempts == max_attempts:
    print("Account locked")
