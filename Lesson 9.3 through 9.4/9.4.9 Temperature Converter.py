# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Convert 0°C to Fahrenheit
celsius_0 = 0
fahrenheit_0 = celsius_to_fahrenheit(celsius_0)
print("0°C in Fahrenheit:", fahrenheit_0)

# Convert 100°C to Fahrenheit
celsius_100 = 100
fahrenheit_100 = celsius_to_fahrenheit(celsius_100)
print("100°C in Fahrenheit:", fahrenheit_100)

# Convert 40°F to Celsius
fahrenheit_40 = 40
celsius_40 = fahrenheit_to_celsius(fahrenheit_40)
print("40°F in Celsius:", celsius_40)

# Convert 80°F to Celsius
fahrenheit_80 = 80
celsius_80 = fahrenheit_to_celsius(fahrenheit_80)
print("80°F in Celsius:", celsius_80)
