# Temperature Converter

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("Select operation:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Enter choice (1/2): ")

if choice == '1':
    celsius = float(input("Enter temperature in Celsius: "))
    print("Temperature in Fahrenheit: ", celsius_to_fahrenheit(celsius))
elif choice == '2':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    print("Temperature in Celsius: ", fahrenheit_to_celsius(fahrenheit))
else:
    print("Invalid input")
