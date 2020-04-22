# for sorting in list we use sort() or sorted('') :-

fruits1 = ['grapes', 'mango', 'apple']
# fruits1.sort()
# print(fruits1)

# for sorting in tuple we use only sorted('') function :-
# but tuples are immutable

fruits2 = ('grapes', 'mango', 'apple')
# fruits2.sort()   # gives error
# print(sorted(fruits2))   # sorted tuple  as sorted list 
# print(fruits2)   # not sort tuple


# for sorting in sets  same as tuples:-

fruits3 = {'grapes', 'mango', 'apple'}
print(sorted(fruits3))


# for sorting in dictionary

guitars = [
    {'model' : 'yamaha f310', 'price'       : 8400},
    {'model' : 'faith naptune', 'price'     :50000},
    {'model' : 'faith apollo venus', 'price':35000},
    {'model' : 'taylor 814ce', 'price'      :450000}
]

sorted_guitar = sorted(guitars, key = lambda d : d['price'], reverse = True)
print(sorted_guitar)