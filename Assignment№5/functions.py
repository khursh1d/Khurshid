
while True:
    #First, i should  get user input
    input_string = input("Please enter string: ")

    #Secondly, this function allows user to terminate the program
    if input_string == "done":
        print("Bye!")
        break

    # Remove special characters 
    special_chars = [".", ",", ":", "!", "?"]
    for char in special_chars:

        input_string = input_string.replace(char, "")
    # Convert word to uppercase
    input_string = input_string.upper()

    # Output the processed string
    print(input_string)
