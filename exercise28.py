class Laptop:
    def __init__(self,name,model,price):
        # instance variable
        self.name = name
        self.model= model
        self.price= price
        self.laptop_name = name + ' ' + model
    def dicount(self,num):
        self.percentage_off = self.price - ((num/100)*self.price)
        return self.percentage_off


l1 = Laptop('dell','inspiron',100)

d = l1.dicount(40)
print(d)