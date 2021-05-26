### This code contains lot of unnecessary comments (which is ugly and bad practice), but i find the solution to this problem a bit tricky for beginners.
# It took me more than an hour to come up with this solution. So, this (ugly) comments are for better understanding the behind the scenes of the code. 

def cross_sum(number):
    # Setting a empty variable sum, for storing final result
    sum = 0
    while number != 0:
        # Dividing the number by 10, gives a decimal nunmber
        temporary_variable_1 = number / 10  # for example: 12/10 = 1.2
        # Performing a floor division, which yields the result without decimal
        number = number // 10   # for example: 12//10 = 1
        # Using round function to round off the substraction. 
        temporary_variable_2 = round(temporary_variable_1 - number, ndigits=1)  # for example: 1.2-1 = 0.2
        # What above equation does is that, it give us the left most digit from the given consecutive number as decimal number with 0 at integer place
        # This can be further multiplied by 10 to get left most digit as integer and keep adding it sum variable 
        sum += (temporary_variable_2 * 10) # for example 0.2*10 = 2
    return print("The cross sum of number is {}".format(int(sum)))


user_input = int(input("Enter the number: "))
cross_sum(user_input)
