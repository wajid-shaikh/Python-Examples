#center method
# name = "harshit" #length = 7

# print(name.center(9,"*")) # 7 + 2 = 9 o/p = *harshit*

name = input("enter your name = ")
star = input("enter number = ")

print(name.center(len(name)+int(star) , "#"))