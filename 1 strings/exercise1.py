# ask user to input 3 numbers and you have to 
# print average of three numbers using string
# formatting

num1,num2,num3 = input('enter three numbers = ').split(' ')
avg = (int(num1) + int(num2) + int(num3))/3
print(f"num1 = {num1}, num2 = {num2}, num3 = {num3}, average = {avg}")