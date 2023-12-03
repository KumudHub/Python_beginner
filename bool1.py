# a function suggesting weather you are sad or not

#def are_you_sad(is_rainy , has_umbrella):  # the variables passed have bolean data type
#    if is_rainy == True and has_umbrella == False:
 
#        return True
#    else:
#        return False
    

# other way to represent the same is 
def are_you_sad(is_rainy, has_umbrella):
    return is_rainy and not has_umbrella

print(are_you_sad(True, False))
print(are_you_sad(False, False))

