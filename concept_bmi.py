print("welcome to bmi calculator")

weight_kg = float(input("Enter weight in kg: "))
height_feet = float(input("Enter feet: "))
height_inch = float(input("Enter inch: "))



#functions for the BMI, Height convertion and others
def bmi(height, weight):
    return weight/(height/100)**2

def feet_inch_to_cm(h_f,h_i):
    h_i += h_f * 12
    return h_i * 2.54

def bmi_result(condition):
    print(f"Your are {condition}")
    
def weight_to(kilogram):
    print(f"You have to {kilogram}")
    


#height and bmi function call
h = feet_inch_to_cm(height_feet, height_inch)
print("Height in cm: %.2f" %h)

BMI = bmi(h, weight_kg)
print("your bmi is: %.3f" %BMI)



#bmi conditions and results
if BMI <= 18.4:
    bmi_result("Under Weight!!")
    weight_to("gain approximately 3 to 8 kilograms")
elif BMI <= 24.9:
    bmi_result("Perfectly Healthy.")
elif BMI <= 29.9:
    bmi_result("Over Weight!!")
    if BMI >= 25:
        weight_to("loose approximately 10 to 15 kilograms")
elif BMI <= 34.9:
    bmi_result("OBESITY CLASS 1!!!")
elif BMI <= 34.9:
    bmi_result("OBESITY CLASS 2!!!")
else :
    bmi_result("OBISTY CLASS 3!!!")    