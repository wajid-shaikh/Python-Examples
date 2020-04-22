# filter function

# by normal function
def is_even(a):
    return a%2 == 0

numbers = [3,4,2,1,5,6,9,8,10]
evens = list(filter(is_even, numbers))
print(evens)

# by lambda expression

# numbers = [3,4,2,1,5,6,9,8,10]
# evens = list(filter(lambda a : a%2 == 0, numbers))
# print(evens)

# by list comprehension

# new_evens = [i for i in numbers if i%2==0]
# print(new_evens)