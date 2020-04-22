#take two comma separated inputs from user
#1. user's name , example - "Harshit"
#2. a single character , "h"

#output - 2 print lines
#1. user's name length
#2. count the character that user inputed(bonus : case inensitive count)

name,char = input("enter name and character = ").split(',')
print(len(name.strip()))
print(name.strip().lower().count(char.strip().lower()))