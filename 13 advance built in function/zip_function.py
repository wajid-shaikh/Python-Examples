# zip function
user_id = ['user1', 'user2', 'user3']
names = ['harshit', 'mohit', 'rohit']
last_names = ['vashistha', 'vashistha', 'sharma']

# zip function gives zip object as tuples

# ('user1', 'harshit'), ('user2', 'mohit')
print(list(zip(user_id, names, last_names)))

# example = [('a', 1),('b', 2)]
# print(dict(example))