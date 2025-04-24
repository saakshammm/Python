# Multiplication Table – Print the multiplication table for a given number
x = int(input("Please enter a number: "))
print(f"The multiplication table of {x} is:")
for i in range (1, 11):
    y = x * i
    print(f"{x} * {i} = {y}")
