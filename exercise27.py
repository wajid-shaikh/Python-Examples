class Laptop:
    def __init__(self,name,model,price):
        # instance variable
        self.name = name
        self.model= model
        self.price= price
        self.laptop_name = name + ' ' + model

l1 = Laptop('dell','inspiron',35000)
l2 = Laptop('HP', 'hyper', 45000)

# print(l1.name,l1.model,l1.price)
# print(l2.name,l2.model,l2.price)

print(l1.laptop_name)