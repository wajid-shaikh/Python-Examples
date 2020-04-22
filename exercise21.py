# define a function tahta take list of strings
# list containing reverse of every string

# NOTE - USE LIST COMPREHENSION because we already did this exercise
# using normal method

# example
# l = ['abc', 'tuv','xyz']
# reverse_string(l) ----> ['cba', 'vut', 'zyx']

# def reverse_string(l):
#     reverse = []
#     for i in l:
#         reverse.append(i[::-1])
#     return reverse

# l = ['abc', 'tuv','xyz']
# # print(reverse_string(l))

# reverse = [i[::-1] for i in l]
# print(reverse)

# with function
def reverse_string(l):
    return[name[::-1] for i in l]

print(reverse_string(['abc', 'tuv', 'xyz']))