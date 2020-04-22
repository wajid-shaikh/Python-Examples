# filter odd even 
# define a function 
# input
# list ---> [1,2,3,4,5,6,7]
# output ---> [[1,3,5,7], [2,4,6]]

# def even_odd(list):
#     even = []
#     odd  = []
#     for i in range(len(list)):
#         if((list[i] % 2) == 0):
#             even.append(list[i])
#             even_list = even
#         else:
#             odd.append(list[i])
#             odd_list = odd
#     new_list = []
#     new_list.append(odd_list)
#     new_list.append(even_list)
#     return new_list

# numbers = input("enter numbers for list = ").split(",")
# number = []
# for i in range(len(numbers)):
#     popped_string = numbers.pop()
#     number.append(int(popped_string))

# number.reverse()
# list = number
# print(even_odd(list))

#############################################################      OR       ########################################

def even_odd(list):
    even = []
    odd  = []
    for i in list:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    result = [odd, even]
    return result

list = [1,2,3,4,5,6,7]

print(even_odd(list))