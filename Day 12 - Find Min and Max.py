# Find Min and Max – Take a list of numbers and find the smallest and largest values
emptyList = list(map(int, input("Enter numbers separated by spaces: ").split()))

minValue = min(emptyList)
maxValue = max(emptyList)

print(f"Minimum value: {minValue}")
print(f"Maximum value: {maxValue}")
