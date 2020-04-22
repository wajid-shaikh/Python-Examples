# looping in tuples
# tuple with one element
# tuple without parenthesis
# tuple unpacking
# list inside tuple
# some functions that you can use with tuples

mixed = (1,2,3,4.0)

# looping in tuples
# for i in mixed:
#     print(i)
# Note - You can use while loop too

# tuple with one element
nums = (1,)
words = ('word1',)
# print(type(nums))
# print(type(words))

# tuple without parenthesis
guitars = 'yamaha', 'baton rouge', 'taylor'
# print(type(guitars))

# tuple unpacking
guitarist = ('Maneli Jamal', 'Eddie Van Der Meer', 'Andrew Foy')
guitarist1, guitarist2, guitarist3 = (guitarist)
# print(guitarist1)

# list inside tuples
favorites = ('southern mongolia', ['Tokyo Ghoul Theme', 'landscape'])
favorites[1].pop()
favorites[1].append("we made it")
# print(favorites)

# min(), max(), sum()
print(min(mixed))
print(max(mixed))
print(sum(mixed))