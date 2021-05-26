def convert(number):
    binary_number = []
    while number != 0:
        # Storing the remainder of division as binary output
        binary_number.insert(0, number % 2)
        # Dividing the number and assigning the resultant qoutient as new number
        number = int(number / 2)
    return print("The binary representation is {}".format(binary_number))
        

user_input = int(input("Enter your desired Decimal number: "))
convert(user_input)