# function returning function
# example 1

def outer_func():
    def inner_func():
        print('inside inner function')
    return inner_func

var = outer_func() # inner_func is now in var
# var()  # givess o/p :- inside inner function

# example 2

# def outer_func2(msg):
#     def inner_func2():
#         print(f'message = {msg}')
#     return inner_func2

# var = outer_func2('hello there !')
# var()

# example 3

def outer_func3(msg1):
    def inner_func3(msg2):
        print(f'message1 = {msg1} and message2 = {msg2}')
    return inner_func3

var = outer_func3('hello there !')
var("i'm using python")