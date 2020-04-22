# LIST COMPREHENSION SUMMARY
# to reduce the line of code 
# square = []
# for i in range(1,11):
#     square.append(i**2)
# print(square)

# or

# square = [i**2 for i in range(1,11)]
# print(square)

# LC for if statement
# even_num = [i for i in range(1,11) if(i%2 == 0)]
# print(even_num)

# LC for if else statement
# number = [i**2 if(i%2 == 0) else -i for i in range(1,11)]
# print(number)

# LC for list inside list
number = [[i for i in range(1,4)] for j in range(1,5)]
print(number)