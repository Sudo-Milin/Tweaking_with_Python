def reverse(input_string):
    # Temporary list to store string, letter-by-letter
    reversed_string_list = []
    reversed_string = ""
    for letter in input_string:
        # Inserting an element(each parsed letter) at '0' position in list, so that resultant list contains string letters in reversed order
        reversed_string_list.insert(0, letter)
    for item in reversed_string_list:
        # Joining each encounterd letter from reverse_string_list to revesed_string variable which results in reversed string 
        reversed_string +=  reversed_string.join(item)
    return print(reversed_string)

user_input_string = input("Enter your string: ")
reverse(user_input_string)


        
        
