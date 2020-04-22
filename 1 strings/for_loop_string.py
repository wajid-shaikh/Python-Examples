# normal method to print single character
# name = "harshit"
# for i in range(len(name)):
#     print(name[i])

# shortcut in python 
# name = "harshit"
# for i in name:
#     print(i)

# 1256 ---> 1+2+5+6

num = input("enter number = ")
total = 0
for i in num: # because string is iterative in python
    total = total + int(i)
print(total)