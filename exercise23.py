# define a function
# input
# num , iterable(tuple , list) conatining numbers as args

# example
# nums = [1,2,3]
# to_power(3, *nums)

# output
# list ---> [1**3, 8, 27]

# if user did'nt pass any args then give a user a message 'hey you did'nt pass'
# args

# else
# return list

# NOTE - USE list comprehension

def to_power(num, *args):
    if args:
        return [i**num for i in args]
    else:
        return 'hey you did\'nt pass any arguments'

numbers = list(range(1,11))
print(to_power(3, *numbers))