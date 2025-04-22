# Reverse a String – Take a user-input string and print it in reverse
userInput = str(input("Please enter a String: "))

# This was done using Slicing
# Syntax: [start:stop:step]
# If you don't give anything, it takes 0 as default.
reversedString = userInput[::-1]
# So, [0:0:-1]

print(f"Reversed string: {reversedString}")