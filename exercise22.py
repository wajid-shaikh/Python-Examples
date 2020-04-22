# num to string
# define a function

# example
# input -----> [True, False, [1,2,3], 1, 1.0, 3]
# output ----> ['1', '1.0', '3']

def num_to_string(l):
    # num = []
    # for i in l:
    #     # print(type(i))
    #     if type(i) == int or type(i) == float:
    #         num.append(str(i))
    # return num
    return [str(i) for i in l if (type(i) == int or type(i) == float)]

list = [True, False, [1,2,3], 1, 1.0, 3]
print(num_to_string(list))