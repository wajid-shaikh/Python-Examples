# add and delete data
user_info = {
    'name' : 'harshit',
    'age'  : 24,
    'fav_tunes'  : ['alan walker', 'shakira'],
    'fav_movies' : ['minions', 'spiderman']
}

# how to add data
# user_info['fav_foods'] = ['biryani', 'chicken nuggets']
# print(user_info)

# pop() method
# popped_item = user_info.pop('fav_tunes')
# print(f"popped item is {popped_item}")
# print(user_info)

# popitem() method deletes last key value pair
popped_item = user_info.popitem()
print(popped_item)
print(user_info)