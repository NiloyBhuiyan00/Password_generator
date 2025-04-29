print("Welcome to the Simple Password Creator!")

# Ask the user for the desired password length
length = int(input("Enter the desired password length: "))

# Let the user create their own password
password = input(f"Enter your password (must be {length} characters long): ")

# Validate the password length
if len(password) == length:
    print(f"Your custom password is: {password}")
elif len(password) < length:
    print(f"Your password is too short! It must be {length} characters long.")
else:
    print(f"Your password is too long! It must be {length} characters long.")
