import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
try:
    password_length = int(input("Enter the desired length of the password: "))

    if password_length <= 0:
        raise ValueError("Password length should be a positive integer.")
    generate_password = generate_password(password_length)
    print("Generated Password: ", generate_password)

except ValueError as e:
    print(f"Error: {e}. Please enter a valid positive integer for the password length")
