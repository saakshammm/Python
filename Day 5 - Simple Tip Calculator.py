# Simple Tip Calculator – Calculate the tip based on the bill amount and tip percentage
bill = float(input("Enter the bill amount: "))
percentage = float(input("Enter the tip percentage: "))

tip = (percentage / 100) * bill
total = bill + tip

print(f"Tip: {tip:.2f}")
print(f"Total amount to pay: {total:.2f}")
