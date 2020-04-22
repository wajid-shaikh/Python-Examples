# exercise on of three
# sum of n natural numbers
# ask a user for natural number(n)
# print total from 1 to n

total = 0
n = int(input("enter number = "))
i = 1
while i <= n:
    total = total + i
    i = i + 1
print(total)