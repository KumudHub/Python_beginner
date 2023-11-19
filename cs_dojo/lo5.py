# another type to use dor loops
a = ["microsoft","apple","banana"]
for i in range(len(a)):
    for j in range(i+1):
        # i = 1 ->  j = 0
        # i = 2 ->  j = 0,1
        # i = 3 ->  j = 0,1,2
        print(a[i])