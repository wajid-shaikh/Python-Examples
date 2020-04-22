# common elements finder function
# define a function which takes two lists as input and return a list
# which conatins common elemetns of both lists

# example 
# input  ---> [1,2,5,8], [1,2,7,6]
# output ---> [1,2]

def common_elements(list1, list2):
    common_list = []
    for i in list1:
        if i in list2:
            common_list.append(i)
    return common_list

list1 = [1,2,5,8,9,16]
list2 = [1,2,7,6,4,11,9]

print(common_elements(list1, list2))