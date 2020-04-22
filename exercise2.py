# ask user to input 3 numbers and you have to 
# print average of three numbers using string
# formatting

num1,num2,num3 = input('enter three numbers = ').split(",")
total = round(((int(num1)+int(num2)+int(num3))/3),4)
print(f"num1 = {num1} \nnum2 = {num2} \nnum3 = {num3} \ntotal = {total}")