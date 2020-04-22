# def a function

# def func(l,**kwargs):
#     if kwargs.get('reverse_str') == True:
#         return [name[::-1].title() for name in l]
#     else:
#         return [name.title() for name in l]
# names = ['harshit', 'mohit']
# # print(func(names))
# print(func(names, reverse_str = True))

def func(l):
    return [i.title() for i in l]
names = ['harshit', 'mohit']
print(func(names))