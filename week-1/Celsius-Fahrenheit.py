def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9
print("1. Celsius to Fahrenheit")
c = float(input("Enter temperature in Celsius: "))
print("Temperature in Fahrenheit:", celsius_to_fahrenheit(c))
print("\n2. Fahrenheit to Celsius")
f = float(input("Enter temperature in Fahrenheit: "))
print("Temperature in Celsius:", fahrenheit_to_celsius(f))
