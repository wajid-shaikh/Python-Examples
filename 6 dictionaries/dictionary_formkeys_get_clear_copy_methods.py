# fromkeys() - used to create dictionaries :-
# d = {'name' : 'unknown', 'age' : 'unknown'}

# d = dict.fromkeys(['name', 'age', 'dob'], 'unknown')
# print(d)

# get() method (useful):- to handls errors we use get() method 
d = {'name' : 'harshit', 'age' : 24}

# print(d['dob']) # gives error because 'dob' key is not present in dictionary

# print(d.get('dob', 'dob not found')) # better to access keys in dictionaries

# if 'name' in d:
#     print('present')
# else:
#     print('not present')

# if d.get('name'):
#     print('present')
# else:
#     print('not present')

# if None ----> False, else ----> Trues

# clear() method :- clear dictionary

# d.clear()
# print(d)

# copy() method :- copy dictionary
# d1 = d.copy() #--- different dictionary
# d1 = d #--- same dictionary
# print(d1.popitem())
# print(d)
# print(d1 == d)