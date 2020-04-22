# class variable
# circle
# area
# circum

class Circle:
    # class variable
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius

    def circum(self):
        return 2*Circle.pi*self.radius
    
    def circleArea(self):
        return Circle.pi*(self.radius**2)

c1 = Circle(5)  # create object of class ' Circle '

# circumferrence = c1.circum()
# print(circumferrence)

area = c1.circleArea()
print(area)
