#BMI calculator
def bmi(name,weight_kg,height_m):
    bmi = weight_kg / (height_m**2)
    print("bmi: ")
    print(bmi)
    if bmi < 25:
        return name + " is not overweight"
    else:
        return name + " is overweight"
    

name1 = "pop"
weight_kg1 = 76
height_m1 = 1.7

name2 = "you"
weight_kg2 = 100
height_m2 = 2

name3 = "me"
weight_kg3 = 59
height_m3 = 1.78


result1 = bmi(name1,weight_kg1,height_m1)
print(result1)
result2 = bmi(name2,weight_kg2,height_m2)
print(result2)
result3 = bmi(name3,weight_kg3,height_m3)
print(result3)
