#Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

#Don't change the code below
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
#Don't change the code above
#Write your code below this line
#weight_as_int = int(weight)
#height_as_float = float(height)
# Using the exponent operator **
#bmi = weight_as_int / height_as_float ** 2
# or using multiplication and PEMDAS
#bmi = weight_as_int / (height_as_float * height_as_float)
#bmi_as_int = int(bmi)
#print(bmi_as_int)
#if bmi_as_int <= 18.5:
#    print("You are underweight.")
#elif bmi_as_int > 18.5 < 25:
#    print("You are normal weight.")
#elif bmi_as_int > 25 < 30:
#    print("You are overweight.")
#elif bmi_as_int > 30 < 35:
#    print("You are obese.")
#else:
#    print("You are clinically obese.")
#Correct solution - didn't change input to float numbers

bmi = round(weight / height ** 2)
if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese.")
else:
    print(f"Your bmi is {bmi}, you are clinically obese.")
