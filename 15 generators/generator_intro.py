# generators
# generators are iterators
# create your first generator with generator 
# 1. generator function
# 2. generator comprehension

def nums(n):
    for i in range(1, n+1):
        yield i
    
numbers = nums(10) # generator

# print(numbers) # <generator object nums at 0x03150570>
for i in numbers:
    print(i)

for i in numbers: # cannot repeat
    print(i)

# normal method :-
# def number(n):
#     for i in range(1, n+1):
#         print(i)
# number(10)

# memory (list) - [..................]
# memory (gen)  - (3)