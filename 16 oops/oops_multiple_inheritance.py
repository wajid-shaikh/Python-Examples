class A:
    def class_a_method(self):
        return 'class A'
    
    def hello(self):
        return 'hello from A class'

class B:
    def class_b_method(self):
        return 'class B'
    
    def hello(self):
        return 'hello from B class'

class C(A , B):
    pass

# instance_a = A()
# print(instance_a.class_a_method())

instance_c = C()
# print(instance_c.class_b_method())
print(instance_c.hello())

##### method resolution order ( MRO ) ####

print(help(C))

# or

print(C.mro())

# or

print(C.__mro__)
