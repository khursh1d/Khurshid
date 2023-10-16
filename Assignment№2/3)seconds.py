#The function `convert_seconds` takes an input parameter `seconds` which is the number of seconds that needs to be converted. 
def convert_seconds(seconds):
    # Calculate hours, minutes, and remaining seconds
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    
    # Print the converted values
    print(f"{hours} hour(s), {minutes} minute(s), {seconds} second(s)")

# Take input from the user
seconds = int(input("Enter the number of seconds: "))

# Call the function to convert and print the result
convert_seconds(seconds)