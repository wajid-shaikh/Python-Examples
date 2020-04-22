# map function

numbers = [1,2,3,4]

# by normal function
# def square(a):
#     return a**2

# squares = list(map(square, numbers))
# print(squares)


# by lambda expression
# squares = list(map(lambda a:a**2, numbers))
# print(squares)


# by list comprehension
# l = [a**2 for a in numbers]
# print(l)


# using normal way
# new_list = []
# for num in numbers:
#     new_list.append(square(num))
# print(new_list)

# str = ['abc', 'abcd', 'abcde']
# length = list(map(len, str)) # map object is iterable but it iterate only once
# print(length)