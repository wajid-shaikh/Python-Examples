# Encapsulation
# Abstraction     =    to hide the complexity from the user
# Some special naming convention
# Name Mangling


#   in python everything is public 
 
# encapsulation = combining data and methods at the same class
# example 
class Phone:
    def __init__(self, brand, model_name, price):
        self.brand      = brand
        self.model_name = model_name
        self._price     = price # private naming convention
    
    def make_a_call(self, phone_number):
        return f"calling... {self.phone_number}"

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def send_message(self):
        pass # twilio

phone1 = Phone('samsung', 'J2', 7000)
# phone1._price = -1000
# print(phone1.__price)
# print(phone1.__dict__)     # data descriptor
# phone1._Phone__price = 1000
# print(phone1._Phone__price)
# jab tak encapsulation nai hogi tab tak abstraction nai hoti
# abstraction = hiding comlexity from user i.e how sorting is performed 
# l = [2,9,1,0]
# l.sort()      # in python tim sort is used      
# print(l)

# special naming conventions###############################
# in python every thing is public 
# dunder means 'underscore underscore'
# _name    # convention of private name
# __name__ # dunder / magic methods
# __name   # not a convention #############################


# Name Mangling changes name _class name __varaible name
# we use '__' in name mangling

# example