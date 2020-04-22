# make a function 'divide'
def divide(a,b):
    return a/b


try:
    print(divide(4,2)) # 2
except TypeError:
    print('please input numbers only')
except ZeroDivisionError:
    print('please don\'t divide by zero')


# print(divide(4,2)) # 2
# print(divide(4,0)) # please don't divide by zero
# print(divide('4',2)) # please input numbers only