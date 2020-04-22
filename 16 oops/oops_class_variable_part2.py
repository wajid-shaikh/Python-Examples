class Laptop:
    discount_percent = 0
    def __init__(self,name,model,price):
        # instance variable
        self.name = name
        self.model= model
        self.price= price
        self.laptop_name = name + ' ' + model
    def discount(self):
        percentage_off = self.price - ((Laptop.discount_percent/100)*self.price)
        return percentage_off


l1 = Laptop('dell','inspiron',100)
l2 = Laptop('hp','hyper',200)

l2.discount_percent = 30

print(l2.__dict__) # print namespace of l2
print(l2.discount())