# BMI < 18.5 Underweight
# 18.5 <= BMI < 25.0 Normal
# 25.0 <= BMI < 30.0 Overweight
# 30.0 <= BMI Obese

weight = float(input("enter your weight in kg: "))
height = float(input("enter your height in m: "))
BMI = weight / height ** 2

if BMI < 18.5:
    print("Underweight")
elif BMI < 25.0:
    print("normal")
elif BMI < 30.0:
    print("overweight")
else:
    print("obese")
