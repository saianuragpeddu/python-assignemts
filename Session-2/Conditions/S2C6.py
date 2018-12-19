def HealthScreen(weight, height):
    bmi = round(weight/(float(height)*height),1)
    retv = "Your BMI is " +str(bmi)
    if bmi >= 25.5:
        retv += " (High Risk)."
    elif bmi >=23 and bmi <=27.4:
        retv += " (Moderate Risk)."
    elif bmi >= 18.5 and bmi <=22.9:
        retv += " (Low Risk)."
    elif bmi <18.5:
        retv += " (Risk of nutritional deficiency diseases)."
    return retv

print(HealthScreen(85, 1.75))
print(HealthScreen(68, 1.65))
