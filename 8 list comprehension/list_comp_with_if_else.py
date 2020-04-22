# list comprehension with if else
nums = [1,2,3,4,5,6,7,8,9,10]
# new_list = [-1,4,-3,8]


def odd_even(l):
    # new_list = []
    # for i in l:
    #     if i%2 == 0:
    #         new_list.append(i*2)
    #     else:
    #         new_list.append(-i)
    # return new_list
    return [i*2 if (i%2 == 0) else -i for i in l]

print(odd_even(nums))