# Body Mass Index (BMI) Calculator

# Calculating function
def calculate_bmi(height, weight):
    # Standard BMI calculating equation
    bmi = weight/(height**2)
    return print("Your BMI is {}".format(bmi))
    
# Taking user input according to specified scale    
scale_input = input("[1] Kilogram(kg), Centimeter(cm)\n[2] Pound(lb), Meters(m)\nSelect scale: ")
if scale_input == "1":
    user_weight_input = float(input("Enter your weight in kilogram(kg): "))
    user_height_input = float(input("Enter your height in centimeter(cm): "))
    user_height_input = float(user_height_input*0.01)
else:
    user_weight_input = float(input("Enter your weight in pound(lb): "))
    user_height_input = float(input("Enter your height in meter(m): "))
    user_weight_input = float(user_weight_input*2.2406)

calculate_bmi(user_height_input, user_weight_input)
