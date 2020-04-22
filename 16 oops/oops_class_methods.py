# class methods
# difference between class methods and instance methods

class Person:
    count_instance = 0    # class variable / class attribute
    def __init__(self, first_name):
        Person.count_instance = Person.count_instance + 1
        self.first_name = first_name
        
    @classmethod
    def count_instances(cls):    # according to convention we use cls as class 
        return f"you have created {cls.count_instance} instances of {cls.__name__} class"

p1 = Person('wajid')
p2 = Person('harshit')
p3 = Person('mohit')

print(Person.count_instance)   # we use class method like this
# o/p = 3 because three object is created