# Decorators - enhance the functionality of other functions

# @ use for decorator

def decorator_function(any_function):
    def wrapper_function():
        print('this is awesome function')
        any_function()
    return wrapper_function


# this is awesome function
def func1():
    print('this is function1')

# this is awesome function
def func2():
    print('this is function2')

# func1() # normal function call 
# func2()

# func1 = decorator_function(func1) # decorator function call
# func1()

# func2 = decorator_function(func2)
# func2()

############################ @ use for decorator
@decorator_function # extends the functionality of func1() function
def func1():
    print('this is function1')

func1()