# exercise
# define a function that takes number(n)
# return a dictionary cube of nunmber from 1 to n

# example
# cube_finder(3)
# {1:1, 2:8, 3:2}

def cube_finder(d):
    cubes = {}
    for i in range(1, d+1):
        cubes[i] = i**3
    return cubes

number = int(input("enter number = "))
print(cube_finder(number))
# cube_finder(number)
