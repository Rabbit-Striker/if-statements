# Simple Login System

# Display a welcoming message
print("Welcome to the Simple Login System")
# Ask the user for a username
user = input("Enter username: ")

# Ask the user for a password
password = input("Enter password: ")

# Check if the username and password are correct
if user == "admin":
    # Check if the password is correct
    if password == "1234":
        print("Access granted")
    else:
        print("Access denied")

else:
    print("Access denied")