# instance method
class Person:
    def __init__(self, first_name, last_name, age):
    # instance variables
        self.first_name = first_name
        self.last_name  = last_name
        self.age        = age

    # instance methods
    def full_name(self):
        return(f"{self.first_name} {self.last_name}")

    def is_above_18(self):
        return self.age>18


p1 = Person('wajid', 'shaikh', 12)
p2 = Person('harshit', 'vashisth', 24)
print(p1.is_above_18())
print(p2.full_name())
# or
# print(Person.full_name(p2))

l = [1,2,3]
# clear, pop
# l.clear()
# list.clear(l)
# print(l)
# l.append(10)
list.append(l,10)
print(l)