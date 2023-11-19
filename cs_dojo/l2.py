# swapping elements in a list
b = ["banana","apple","microsoft"]

print(b)

temp = b[0]
b[0] = b[2]
b[2] = temp

print(b)

# another way to swap any list elements
b[0],b[2]=b[2],b[0]
print(b)
