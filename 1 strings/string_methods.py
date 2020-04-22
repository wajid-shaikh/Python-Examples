#string methods part one

name = "HaRsHiT vASHISThA"

# 1. len() function
print(len(name)) #gives length of string including white spaces
#o/p = 17

# 2. lower() method converts all capital letters to lower letters
print(name.lower()) #for methods we use '.'
#o/p = harshit vashistha

# 3. upper() method converts all small letters to capital letters
print(name.upper()) #for methods we use '.'
#o/p = HARSHIT VASHISTHA

# 4. title() method converts first character of every word to capital
print(name.title())
#o/p = Harshit Vashistha

# 5. count() method counts the character repitation in string
print(name.count("h")) #o/p = 1
print(name.count("H")) #o/p = 3
