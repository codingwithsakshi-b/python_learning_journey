#BMI calculator
wt = float(input("enter your weight in kg:"))
ht = float(input("enter your height in m:"))

ht_bmi = ht**2
BMI = wt/ht_bmi

if(BMI < 18.5):
    print("you are underweight")
elif(BMI>18.5 and BMI<24.9):
    print("you have a normal weight")
elif(BMI>24.9 and BMI<29.9):
    print("you are overweight")
else:
    print("you are obese")
