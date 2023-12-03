# learning more about lsit 
# print a list including squares of all integers from 1 to 6


el = []
for x in range(1,7):
    el.append(x ** 2)

print(el)

# now using the list comprehension for the above question

el = [x ** 2 for x in range(1,7)]
print(el)