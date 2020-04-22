# can we derive more than one class from base class ?
# multilevel inheritance
# method resolution order (MRO)
# method overriding
# isinstance(), issubclass()

# multilevel inheritance ##################################
class Phone: # base class / parent class
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price, 0)

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def make_a_call(self, number):
        return f"calling {number}..."


class Smartphone(Phone): # derived class / child class
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera):
        # two ways
        # Phone.__init__(self,brand,model_name,price) # uncommon way
        super().__init__(brand,model_name,price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

    def full_name(self):
        return f"{self.brand} {self.model_name} and price is {self._price}"



class FlagshipPhone(Smartphone):
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera, front_camera):
        super().__init__(brand, model_name, price, ram, internal_memory, rear_camera)
        self.front_camera = front_camera

    def full_name(self):
        return f"{self.brand} {self.model_name} and price is {self._price} and front camera = {self.front_camera}"


phone      = Phone('nokia', '1100', 1000)
smartphone = Smartphone('onePlus', '5', 30000, '6 GB', '64 GB', '20 MP')
flagphone  = FlagshipPhone('onePlus', '5', 30000, '6 GB', '64 GB', '20 MP', '16 MP')

# print(oneplus.full_name())

# method resolution order (MRO) #############################
# print(smartphone.full_name())
# print(help(Smartphone)) # MRO of Smartphone class
# print(oneplus.full_name())
# print(help(FlagshipPhone)) # MRO of FlagshipPhone class

# isinstance(), issubclass() ################################

# print(isinstance(flagphone, Phone))      # True
# print(isinstance(phone, FlagshipPhone))  # false

print(issubclass(Smartphone, FlagshipPhone)) # False
print(issubclass(FlagshipPhone, Smartphone)) # True

