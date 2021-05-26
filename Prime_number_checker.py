
def check_prime(user_input):
    # Variable to check if the number is prime. If divisible != 2 then not prime
    divisible = 0
    # Count variable as a divisor, which keeps on increamenting
    count = 1
    for i in range(user_input):
        if user_input % count == 0:
            divisible += 1
        count += 1

    if divisible == 2:
        print("The number {} is Prime!".format(user_input))
    else:
        print("The number {} is not Prime!".format(user_input))

number = int(input("Please enter your desired number: "))
check_prime(number)