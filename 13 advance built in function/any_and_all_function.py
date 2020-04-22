# any , all function

numbers1 = [2,4,6,9,10]
numbers2 = [1,2,3,4,5,6]
print(all([num%2==0 for num in numbers1]))
print(any([num%2==0 for num in numbers1]))

# even = []
# for num in numbers1:
#     even.append(num%2==0)
# all() function checks whether all values in iterables is true then
# return True
# else 
# return False
# print(all([True, False, True, True, True])) #---> if all values are true then it returns True


# any() function checks atleast 1 iterable value is true then it
# return True
# else
# return False
# print(any([True, False, True, True, True])) #---> if single values are true then it returns True