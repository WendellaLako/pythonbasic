weight_in_kg = float(input('Please enter your weight in KG: ')) #string
height_in_m = float(input('Please enter your height in m:')) #string

bmi_formula = weight_in_kg / height_in_m ** 2

if bmi_formula <= 18.5:
    print("You Underweight")
elif bmi_formula >= 18.5 and bmi_formula <= 24.9:
    print("Normal weight")
elif bmi_formula >= 25.0 and bmi_formula <= 29.9:
    print("Overweight")
elif bmi_formula >= 30.5 and bmi_formula <= 34.9:
    print("Obesity Class I")
elif bmi_formula>= 35.5 and bmi_formula <= 39.9:
    print("Obesity Class II")
else:
    print("Obesity Class III")