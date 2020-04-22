# dictionaries intro
# Q - why we use dictionaries ?
# A - Because of limitations of lists , lists are not enough to represent
# real data

# Example
user = ['Harshit', 24, ['coco', 'kimi no na wa'], ['awakening', 'fairy tale']]
# this list contains user name , age , fav movies , fav tunes
# you can do this but this is not  a good way to do this.

# Q - what are dictionaries
# A - unordered collections of data in key : value pair.

# how to create dictionaries
user = {'name' : 'Harshit', 'age' : 24}
# print(user)
# print(type(user))

# second method to create dictionaries
user1 = dict(name = 'Harshit', age = 24)
# print(user1)

# how to access data from dictionaries
# Note - there is no indexing because of unordered collections of data
# print(user['name'])
# print(user['age'])

# which type of data dictionary can store ?
# anything
# numbers, strings, list, dictionary
#user_info = {'name' : 'harshit','age'  : 24,'fav_movies' : ['coco', 'kimi no na wa'],'fav_tunes'  : ['awakening', 'fairy tale']}

#or 

user_info = {
    'name' : 'harshit',
    'age'  : 24,
    'fav_movies' : ['coco', 'kimi no na wa'],
    'fav_tunes'  : ['awakening', 'fairy tale'],
}

# print(user_info['fav_movies'])


# How to add data to empty dictionary
user_info2 = {}
user_info2['name'] = 'mohit'
user_info2['age'] = 19
# print(user_info2)


###################################### practice ############################
d = {
    'name' : 'shubham',
    'age'  : 24,
    'movies': ['abc','xyz']
    }
# print(d['age'])
#or
# print(d.get('age'))

d['foods'] = ['biryani', 'chicken nuggets']

print(d)