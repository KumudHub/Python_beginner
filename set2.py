# now we will remove duplicates in a set using sets

a = [1,1,2,4,2]

new_a = set()   # create an empty set

for x in a:     # iterate through the list 
    new_a.add(x)       # add the components of the list in the epmty set created
 
print(new_a)


# now we will create a list from the set created just above

new_list = list()
for x in new_a:
    new_list.append(x)

print(new_list)