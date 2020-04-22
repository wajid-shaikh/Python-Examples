# it's very simple same as list comprehension
# instead of [] use ()
# example

# LC method for square of numbers

square = [i**2 for i in range(1,11)]
print(square)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# GC method for square of numbers

square = (i**2 for i in range(1,11))
print(square)  # <generator object <genexpr> at 0x02BFC270>

for num in square:
    print(num)