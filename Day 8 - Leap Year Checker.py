# Leap Year Checker – Check if a given year is a leap year
inputYear = int(input("Enter the year: "))

if inputYear % 4 == 0:
    if inputYear % 100 == 0:
        if inputYear % 400 == 0:
            print(f"{inputYear} is a leap year.")
        else:
            print(f"{inputYear} is not a leap year.")
    else:
        print(f"{inputYear} is a leap year.")
else:
    print(f"{inputYear} is not a leap year.")