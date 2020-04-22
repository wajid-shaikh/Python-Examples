# define generator function
# take one number as argument
# generate a sequence of even numbers from 1 to that number
# only even numbers

def generator(n):
    for i in range(2, n+1, 2):
        yield i

gen = generator(5)

for num in gen:
        print(num)