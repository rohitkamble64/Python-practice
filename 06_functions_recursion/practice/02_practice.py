# WAP to convert temperature from Celsius to Fahrenheit and vice versa using functions

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"Temperature in Fahrenheit: {fahrenheit}")

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = fahrenheit_to_celsius(fahrenheit) 
print(f"Temperature in Celsius: {round(celsius, 2)} °C")