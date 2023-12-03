# find the sum of the unique elements stored in a list

list = [1,3,4,1,3]

new_set = set()
for x in list:
    new_set.add(x)
print(new_set)


sum = 0

for a in new_set:
    sum = sum + a

print(sum)