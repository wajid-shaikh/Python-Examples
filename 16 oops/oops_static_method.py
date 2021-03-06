# static method has logical connection with class
# static method does not require any 'arguments'
class Person:
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

    @staticmethod
    def hello():
        print('hello, static method called')

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

p1 = Person('wajid', 'shaikh', 23)
Person.hello() # static method get called
# p2 = Person.from_string('wajid, shaikh, 23')
# print(Person.count_instance)
print(p1.first_name)
# print(p1.full_name())