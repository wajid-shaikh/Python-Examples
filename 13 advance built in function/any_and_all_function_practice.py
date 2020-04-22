# any all function

# by normal method
# def my_sum(*args):
#     l = []
#     for arg in args:
#         l.append(type(arg) == int or type(arg) == float) 
#         # print(l) # prints --> [True, True, True, True]
    
#     if all(l): # returns true if all 'l' are true 
#         total = 0
#         for num in args:
#             total = total + num
#         return total
#     else:
#         return "wrong input"
# print(my_sum(1,2,34,5.5))

# by list Comprehension method
def my_sum(*args):
    if all([(type(arg) == int or type(arg) == float) for arg in args]):
        total = 0
        for num in args:
            total = total + num
        return total
    else:
        return "wrong input"
print(my_sum(1,2,34,5.5))