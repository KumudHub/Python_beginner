#bmi calculater
name = "KS"
height_m = 2.3
weight_kg = 89

bmi = weight_kg / (height_m**2)
print("bmi: ")
print(bmi)
if bmi>25:
    print(name)
    print("is overweight")
else:
    print(name)
    print("is not overweight")
