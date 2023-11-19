# usage of break statement in for loop
a = [5,4,4,3,1,-2,-3,-5]
total =0
for i in a:
    if i <= 0:
        break
    total = total + i
print(total)

