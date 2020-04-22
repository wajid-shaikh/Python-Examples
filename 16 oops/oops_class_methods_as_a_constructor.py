# class methods
# difference between class methods and instance methods

class Person:
    # class variable / class attribute
    count_instance = 0
    def __init__(self, first_name, last_name, age):
        Person.count_instance = Person.count_instance + 1
        self.first_name = first_name
        self.last_name  = last_name
        self.age        = age

    @classmethod
    def from_string(cls, string):
        first,last,age = string.split(',')
        return cls(first,last,age)    

    @classmethod
    def count_instances(cls):
        return f"you have created {cls.count_instance} instances of {cls.__name__} class"

p1 = Person('wajid', 'shaikh', 23)
p2 = Person.from_string('wajid, shaikh, 23')
print(Person.count_instance)
print(p1.first_name)