# list chapter summary
# list is a data structure that can hold any type of data

# create a list
words = ['words1', 'words2']

# you can store anything inside list
mixed = [1,2,3,[4,5,6],'seven',8.0,None]

# list is ordered collection of items
print(mixed[0]) # output = 1
print(mixed[3]) # output = [4,5,6]

# add data to our list
# append method

# mixed.append('10')
# print(mixed) # output = [1,2,3,[4,5,6],'seven',8.0,None,'10']

# mixed.append([10,20,30])
# print(mixed) # output = [1,2,3,[4,5,6],'seven',8.0,None,[10,20,30]]

# mixed.extend([10,20,30])
# print(mixed) # output = [1,2,3,[4,5,6],'seven',8.0,None,10,20,30]

# join two list
# l = list1 + list2

# mixed.insert(1, 'inserted') # output = [1,'inserted',2,3,[4,5,6],'seven',8.0,None,10,20,30]
# print(mixed)

# remove data from list
# popped = mixed.pop() # remove last item # pop() returns a popped value
# popped = mixed.pop(1) # remove item at position 1

# remove
# mixed.remove('seven')

# del statement
# del mixed[3]

# loop in list

# for i in mixed:
#     print(i)