# you have to have a complete understanding of functions,
# first class function / closure
# then finally we will learn about decorators

def square(a):
    return a**2

s = square # assign square function to another variable
# print(s(7))
print(s.__name__) # gives function name i.e square
print(square.__name__) # gives function name i.e square
# both are on same memory location
print(s)     # <function square at 0x007EB660>
print(square)# <function square at 0x007EB660>