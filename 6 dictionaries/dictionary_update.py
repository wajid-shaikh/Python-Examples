# if we to add another dictionary in one dictionary then we use update() method 
user_info = {
    'name' : 'harshit',
    'age'  : 24,
    'fav_movies' : ['minions', 'spiderman'],
    'fav_tunes'  : ['alan walker', 'shakira'],
}

# more_info = {'name' : 'harsh', 'state' : 'Haryana', 'hobbies' : ['coding', 'reading', 'guitar']}

user_info.update({'name': 'shubham'})
print(user_info)