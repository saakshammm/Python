# Even or Odd – Check whether a number is even or odd.
num = int(input("Please enter a number: "))
res = num % 2
if res == 0:
    print("The number is even.")
else:
    print("The number is odd.")
