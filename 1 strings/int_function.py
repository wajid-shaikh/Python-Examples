num1 = int(input('enter first number = ')) # "4" to convert in integer use int()
num2 = int(input('enter second number= ')) # "4" to convert in integer use int()
total = num1 + num2 # 8
#now total is integer convert it to string
# we cannot concatenate string with integer
print('total = ' + str(total))

# int()
# "4" --> 4

# str()
# 4 --> "4"

#float()
# "4" --> 4.0

#we can add int value with float value o/p = float value
#e.g 
num3 = int("4")
num4 = float("4")
print(num3 + num4)