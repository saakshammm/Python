# Basic Password Checker – Ask the user to enter a password and verify if it meets simple security criteria

# To create a Basic Password Checker, we can verify if the entered password meets simple security criteria such as:
# 1. It must be at least 8 characters long.
# 2. It must contain at least one uppercase letter.
# 3. It must contain at least one lowercase letter.
# 4. It must contain at least one digit.
# 5. It must contain at least one special character (like @, #, etc.).

import re

password = str(input("Enter your password: "))

if len(password) < 8:
    print("Password must be at least 8 characters long.")
elif not re.search(r'[A-Z]', password):
    print("Password must have an uppercase character.")
elif not re.search(r'[a-z]', password):
    print("Password must have a lowercase character.")
elif not re.search(r'[0-9]', password):
    print("Password must have a numeric character.")
elif not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
    print("Password must have a special character.")
else:
    print("You're a genius!")

