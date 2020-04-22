# THIS IS CHALLENGE

# define a function take any no of lists containing number
# [1,2,3] , [4,5,6] , [7,8,9]
# return average
# (1+4+7)/3 , (2,5,8)/3 , (3,6,9)/3

# try to make this anonymous function in one line using lambda


def average_finder(*args):
    l = []
    for i in zip(*args):
        l.append(sum(i)/len(i))
    return l
print(average_finder([1,2,3] , [4,5,6]))

# OR

# average_finder = lambda *args : [sum(i)/len(i) for i in zip(*args)]
# print(average_finder([1,2,3] , [4,5,6]))