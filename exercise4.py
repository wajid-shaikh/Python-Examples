#take two comma separated inputs from user
#1. user's name , example - "Harshit"
#2. a single character , "h"

#output - 2 print lines
#1. user's name length
#2. count the character that user inputed(bonus : case inensitive count)

name,char = input("enter comma separated name and character = ").split(",")
print(f"length of your name is {len(name.strip())}")
print(f"character count : {name.strip().lower().count(char.strip().lower())}")