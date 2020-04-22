# sum fromo 1 to 10
# 1 + 2 + 3 + ... + 10

# total = 0
# for i in range(1, 11):
#     total = total + i
# print(total)

n = int(input("enter number = "))
total = 0
for i in range(1, n+1):
    total = total + i
print(total)