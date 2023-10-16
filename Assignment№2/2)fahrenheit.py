
# Function to convert Celsius to Fahrenheit
#This code defines a function called `celsius_to_fahrenheit` which takes a temperature in Celsius as input and returns the temperature in Fahrenheit.
def celsius_to_fahrenheit(celsius):
    # This is formula which calculates the Fahrenheit equivalent of Celsius, which is in the presentation
    fahrenheit = (celsius * 9/5) + 32
    #It then returns the calculated Fahrenheit value.
    return fahrenheit

# This code accepts temperature in Celsius from the user
# Again I used "float" data type to do the data more understandable
celsius = float(input("Enter temperature in Celsius: "))

# Converts Celsius to Fahrenheit
fahrenheit = celsius_to_fahrenheit(celsius)

# Finally displays the converted temperature
print("Temperature in Fahrenheit:", fahrenheit)
