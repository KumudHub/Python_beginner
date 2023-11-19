# deletion from a list
a = [3,5,-1]

a.append(1)
a.append("hello")

a.append([9,8])
print(a)

a.pop()
print(a)

a.pop()
print(a)

print(a[0])
a[0] = 100

print(a)