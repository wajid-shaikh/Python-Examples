# function returning two values
def func(int1, int2):
    add = int1 + int2
    mul = int1 * int2
    return add, mul

# print(func(6,2))
add, mul = func(6, 2)
print(add)
print(mul)