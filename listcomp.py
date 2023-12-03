# it is about the list comprehensions learning that is short method instead for iteration purposes

a = [1,3,5,7,9,11]

b = []
b.append(10)
b.append(20)

print(b)

c = []
for x in a:
    c.append(x * 2)

print(c)

# now doing the same thing with simpler syntax

d = [x * 2 for x in a]
print(d)