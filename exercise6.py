# EXERCISE - WATCH COCO
# Ask user's name and age
# If user's name start with ('a' or 'A') and age is above 10 then
# print 'you can watch coco movie' 
# Else print 'sorry, you cannot watch coco'

name = input('enter your name = ')
age  = int(input('enter your age = '))

if ( name[0] == 'a' or name[0] == 'A' ) and age >= 10:
    print('you can see coco movie')
else:
    print('sorry, you cannot watch coco')