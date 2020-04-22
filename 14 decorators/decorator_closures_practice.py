# function returning function 
# also called as (closure)

# different operations using same function 
def to_power(x): # x = 2
    def calc_power(n): # n = 3 then 3**2 = 9
        return n**x
    return calc_power

square = to_power(2)
print(square(5))

cube = to_power(3)
print(cube(5))