# *args with normal parameter

def multiply_nums(num,*args):
    multiply = 1
    for i in args:
        multiply = multiply * i
    return multiply

print(multiply_nums(2,3,3,4))