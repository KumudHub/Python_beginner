#can you compute all multiples of 3 and 5 in a range less than 100

#print(list(range(1,100)))
multiples=[]
for i in range(1,100):
    if i % 3 == 0 or i % 5 ==0: 
        multiples.append(i)
print(multiples)