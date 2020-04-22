# practice for loop
# ask user name and count each character
# "Harshit Vashisth"
# H : 1
# a : 2
# r : 1
# s : 3
# h : 3
# i : 2
# t : 2
#   : 1
# V : 1

name = input("enter your name = ")
n = len(name)
temp_var = ""
for i in range(0, n):
    if name[i] not in temp_var:
        temp_var = temp_var + name[i]
        print(f" {name[i]} : {name.count(name[i])}")