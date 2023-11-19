# now same question of adding all the negative elements in the list where numbers are given in descending order

a = [7,5,4,4,3,1,-2,-3,-5,-7]
total = 0
i = len(a)-1
while True:
    if a[i]<=0:
        total = total + a[i]
        i = i-1
    else:
        break
print(total)
        