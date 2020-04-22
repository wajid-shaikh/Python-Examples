# define a function which takes two numbers as a input and
# return greater of two numbers

def numbers(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    elif c>a and c>b:
        return c
    else:
        return "all are equal"

num1 = int(input("num1 = "))
num2 = int(input("num2 = "))
num3 = int(input("num3 = "))

bigger = numbers(num1,num2,num3)
print(f"{bigger} is greater")