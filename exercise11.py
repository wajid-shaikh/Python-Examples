# Define is_palindrome function that take one word in string as input
# and return True if it is palindrome else return False

# palindrome - word that reads same backwards as forwards

# example
# is_palindrome("madam") --- >True
# is_palindrome("naman") --- >True
# is_palindrome("horse") --- >False

# logic (algorithm)
# step 1 -> reverse the string
# step 2 -> compare reversed string with original string

def is_palindrome(name):
    return name == name[::-1]

n =  input("enter name = ")
result = is_palindrome(n)
if result:
    print(f"{n} is palindrome")
else:
    print(f"{n} is not palindrome")