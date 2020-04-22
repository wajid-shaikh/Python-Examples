# map method 
def square(a):
    return a**2

l = [1,2,3,4]
# print(list(map(square, l))) # in built method map() method takes function as an argument

# pass function as an argument to user define function
def my_map(func, l): # my_map takes func function as argument
    new_list = []
    for item in l:
        new_list.append(func(item))
    return new_list

print(my_map(square, l))

# pass function as an argument to user define function
# same thing by using lambda expression
# instead of square we use lambda expression

# def my_map(func, l):
#     new_list = []
#     for item in l:
#         new_list.append(func(item))
#     return new_list

# print(my_map(lambda a : a**2, l))

# same thing by list comprehension
# def my_map(func, l):
#     return [func(item) for item in l]

# print(my_map(lambda a : a**2, l))