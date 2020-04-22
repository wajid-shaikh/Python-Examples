# define a function that take list of words as argument and
# return list with reverse of every elements in that list

# example 
# ['abc', 'tuv', 'xyz'] ---> ['cba', 'vut', 'zyx']

def reverse_list(list):
    reverse = []
    for i in list:
        reverse.append(i[::-1])
    return reverse

str_list = ['abc','tuv','xyz']
print(reverse_list(str_list))