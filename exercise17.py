# last exercise
# function to check count of list inside list
# example
# [1, 2, 3, [1, 2], [3, 4]]

def check_count_of_list_inside_list(l):
    count = 0
    for i in l:
        if type(i) == type(list):
            count = count + 1
        # print(type(i))
    return count

list = [1, 2, 3, [1, 2], [3, 4], [5, 6]]

print(check_count_of_list_inside_list(list))