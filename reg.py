import re
# Function to validate email address format
def is_valid_email(email):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(pattern, email)

# Function to validate phone number format (Egyptian phone numbers only)
def is_valid_phone(phone):
    pattern = r'^01[0-9]{9}$'
    return re.match(pattern, phone)




# Function to register a new user
def register():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email address: ")
    while not is_valid_email(email):
        email = input("Invalid email address. Please enter a valid email address: ")
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")
    while password != confirm_password:
        confirm_password = input("Passwords do not match. Please confirm your password again: ")
    phone = input("Enter your mobile phone number: ")
    while not is_valid_phone(phone):
        phone = input("Invalid phone number. Please enter a valid Egyptian phone number: ")
    with open("users.txt", "a") as file:
        file.write("{} {} {} {} {} \n".format(first_name, last_name, email, password, phone ))
    print("Registration successful.")

# Function to log in an existing user
def login():
    email = input("Enter your email address: ")
    password = input("Enter your password: ")

    with open("users.txt", "r") as file:
        for line in file:
            user_info = line.strip().split()
            if user_info[2] == email and user_info[3] == password:
                print("Login successful.")
                print("Welcome, {} {}!".format(user_info[0], user_info[1]))
                return
    print("Invalid email or password. Please try again.")


