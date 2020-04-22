from functools import wraps
def only_int_allow(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        data_types = []
        for arg in args:
            data_types.append(type(arg)==int)
        if all(data_types):
            return function(*args, **kwargs)
        else:
            return 'Invalid arguments'
    return wrapper

@only_int_allow
def add_all(*args):
    total = 0
    for i in args:
        total = total + i
    return total

print(add_all(1,2,3,4,5,989,45))