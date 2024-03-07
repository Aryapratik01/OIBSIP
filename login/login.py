import hashlib

users = {}

def register():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    users[username] = hashed_password
    print("Registration successful!")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users:
        entered_password = hashlib.sha256(password.encode()).hexdigest()
        if entered_password == users[username]:
            print("Login successful!")
            return True
        else:
            print("Incorrect password. Please try again.")
    else:
        print("Username not found. Please register.")

    return False

def secured_page():
    print("Welcome to the secured page!")

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        register()
    elif choice == '2':
        if login():
            secured_page()
            break
    elif choice == '3':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        
