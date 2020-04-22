# in keyword and iterations in dictionary

user_info = {
    'name' : 'harshit',
    'age'  : 24,
    'fav_movies' : ['coco', 'minions'],
    'fav_tunes'  : ['alan walker', 'shakira'],
}

# check if key exist in dictionary :-
# if 'name' in user_info:
#     print('present')
# else:
#     print('not present')

# check if value exist in dictionary :-
# if 24 in user_info.values():
#     print('present')
# else:
#     print('not present')

# loops in dictionaries  :-
# for values :-
# for i in user_info.values():
#     print(i)

# for keys :-
# for i in user_info.keys():
#     print(i)

# values method:-
# user_info_values = user_info.values()
# print(user_info_values)
# print(type(user_info_values))

# keys method:-
# user_info_keys = user_info.keys()
# print(user_info_keys)
# print(type(user_info_keys))

# loops in dictionaries:-
# for i in user_info:
#     print(user_info[i])

# items method:-
user_items = user_info.items()
print(user_items)
# print(type(user_items))
# [('name', 'harshit'), ('age', 24), ('fav_movies', ['coco', 'minions']), ('fav_tunes', ['alan walker', 'shakira'])]

# for key, value in user_info.items():
#     print(f"key = {key} and value = {value}")