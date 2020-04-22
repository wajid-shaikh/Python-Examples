# define a function which will take list as a argument and this function
# will return a reversed list

# example 
# [1,2,3,4] ---> [4,3,2,1]
# ['word1', 'word2'] ---> ['word2', 'word1']

# Note you simply do this with reverse method or [::-1]

# but try to do this with the help of append and pop method

def reverse_list(list):
    new_list = []
    for i in range(len(list)):
        popped_number = list.pop()
        new_list.append(popped_number)
    return new_list

numbers = [1,2,3,4]
print(reverse_list(numbers))