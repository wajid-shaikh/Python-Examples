# special magic methods / dunder methods
# operator overloading
# polymorphism

class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def phone_name(self):
        return f"{self.brand} {self.model}"
    
    # str , repr
    def __str__(self):     # nicely formatted string
        return f'{self.brand} {self.model}'

    def __repr__(self):    # on return we can create an object also
        return f'phone(\'{self.brand}\', \'{self.model}\', \'{self.price}\')'

my_phone = Phone('Nokia', '1100', 1000)
# print(str(my_phone))   # call as function also
# print(repr(my_phone))  # call as function also
print(my_phone.__repr__())
