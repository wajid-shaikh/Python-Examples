# OBJECTIVES
# WHAT IS CLASS
# HOW TO CREATE AN CLASS
# WHAT IS INIT METHOD , CONSTRUCTOR
# WHAT ARE ATTRIBUTES,INSTANCE VARIABLES
# HOW TO CREATE OUR OBJECT

class Person:
    def __init__(self,first_name,last_name,age):
        # instance variable
        self.first_name = first_name # self represents an object i.e p1 or p2 
        self.last_name  = last_name
        self.age        = age

p1 = Person('wajid', 'shaikh', 23)
p2 = Person('majid', 'shaikh', 29)

print(p1.first_name)
print(p2.first_name)
# print(p1)  # gives object :- <__main__.Person object at 0x02EE44F0>