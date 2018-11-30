def BMI(weight, height):
    return "%0.1f" % (float(weight) / (height * height))

print(BMI(63,1.7))
print(BMI(110,2))
print(BMI(70,1.7))
