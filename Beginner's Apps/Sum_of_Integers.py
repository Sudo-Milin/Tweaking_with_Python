def add_it_up():
    sum = 0 
    number = input("Enter your desired number: ")
    try:
        # Convert user input in 'try' block to 'int' using type casting. 
        for integer in range(int(number)+1):
            sum += integer
        result =  sum
    # If user enters value other than 'int'
    except ValueError:
        result = 0
    
    return result

print(add_it_up())