# Sum of Digits – Take a number input and find the sum of its digits
num = input("Enter a number: ")

if num.isdigit():
    sumOfDigits = 0

    for digit in num:
        sumOfDigits += int(digit)

    print(f"Sum of digits: {sumOfDigits}")
else:
    print("Invalid input! Please enter a valid number.")

