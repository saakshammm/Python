# Unit Converter – Convert temperature (Celsius/Fahrenheit) and distance (km/miles).
c = float(input("Enter a number to be converted from Celsius to Fahrenheit: "))
f = (c * 9/5) + 32
print(f"The temperature from Celsius to Fahrenheit is: {f}")

km = float(input("Enter the distance to be converted from KMs to Miles: "))
m = km * 0.62137119
print(f"The distance in Miles is: {m}")
