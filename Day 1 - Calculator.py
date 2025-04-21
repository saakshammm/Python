# Basic Calculator – Perform addition, subtraction, multiplication, and division based on user input.
num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))

operationPerformed = input("What operation is to be performed on these two numbers? (+, -, / or *): ")

if operationPerformed == "+":
    result = num1 + num2
    print(f"The addition of {num1} and {num2} is:", result)
elif operationPerformed == "-":
    result = num1 - num2
    print(f"The subtraction of {num1} and {num2} is:", result)
elif operationPerformed == "/":
    result = num1 / num2
    print(f"The division of {num1} and {num2} is:", result)
elif operationPerformed == "*":
    result = num1 * num2
    print(f"The multiplication of {num1} and {num2} is:", result)
else:
    print("Please try again.")