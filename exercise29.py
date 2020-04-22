class Person:
    count_instance = 0
    def __init__(self, name): # called as constructor
        self.name = name
        Person.count_instance = Person.count_instance + 1

p1 = Person('wajid')
p2 = Person('shaikh')
p3 = Person('shaikh')
p4 = Person('shaikh')
p5 = Person('shaikh')
p6 = Person('shaikh')
print(Person.count_instance)