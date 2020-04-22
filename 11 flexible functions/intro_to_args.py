# make flexible functions
# *operator
# *args
# * --> because of this operator we can pass multiple parameter to the function
# example

# def total(a,b):  # this function accepts only 2 parameters
#     return a+b
# print(total(3,4))

def total(*args): # now this creates a tuple value like (1,2,3,4)
    total = 0
    for num in args:
        total = total + num
    return total

print(total(1,2,3,4))
