# define a function which will take list containing numbers as input
# return list containing square of every elements

# example 
# numbers = [1,2,3,4]
# square_list(numbers) ----> return ----> [1,2,9,16]

def square_list(list):
    square = []
    for i in list:
        square.append(i**2)
    return square
numbers = [1,2,3,4]
data = square_list(numbers)
print(data)