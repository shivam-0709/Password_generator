# Password Generator with Levels

import string
import random

def generate_password(length, level):
    letters = string.ascii_letters
    numbers = string.digits
    symbols = "!@#$%&*"

    if level == 1:
        chars = letters
    elif level == 2:
        chars = letters + numbers
    elif level == 3:
        chars = letters + numbers + symbols
    else:
        return None

    # Ensure strong password has all types
    password = []
    if level == 2 and length >= 2:
        password.append(random.choice(letters))
        password.append(random.choice(numbers))
    elif level == 3 and length >= 3:
        password.append(random.choice(letters))
        password.append(random.choice(numbers))
        password.append(random.choice(symbols))

    # Fill the rest
    while len(password) < length:
        password.append(random.choice(chars))

    # Shuffle for randomness
    random.shuffle(password)
    return "".join(password)


print('Lets create password -- 1=Easy, 2=Medium, 3=Hard')

while True:
    try:
        level = int(input("Enter the level: "))
        length = int(input("Enter password length: "))
        pwd = generate_password(length, level)
        if pwd:
            print(f"Generated Password: {pwd}")
        else:
            print("Invalid level. Please type 1, 2, or 3 only.")
    except ValueError:
        print("Please enter numbers only.")
        continue

    again = input("Wanna play again? (y/n): ").lower()
    if again != 'y':
        break

print("Thanks for using the Password Generator!")