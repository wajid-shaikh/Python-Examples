# replace() method
#---------------------------------------------------------
string = "she is beautiful and she is good dancer"
print(string.replace(" " , "_")) # replace ' ' by '_' 

print(string.replace("is" , "was")) # replace 'is' by 'was'

print(string.replace("is" , "was" , 1)) # replace 1 'is'

print(string.replace("is" , "was" , 2)) # replace 2 'is' 

#find() method
#---------------------------------------------------------

print(string.find("is")) # finds the position of is o/p = 4

is_pos1 = string.find("is") # is_pos1 ---> number
is_pos2 = string.find("is",is_pos1 + 1)
print(is_pos2)