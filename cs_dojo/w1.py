# sum of only posotive numbers in any list
# usage of function for the size of list
a = [5,4,4,3,1,-2,-3,-5]
total =0
i = 0

while i<len(a) and a[i]>0: #usage of inbuilt function to find out length of any list
    total= total + a[i]
    i = i+1
print(total)