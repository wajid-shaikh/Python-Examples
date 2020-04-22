# l1 = [1,9,11,7]
# l2 = [2,4,6,8]
new_list = []
l = [(1,6), (9,4), (5,2), (3,7)]
# * operator with zip to unpack the 'l' list into two list

l1,l2 = list(zip(*l))
# print(l1) # (1, 9, 5, 3)
# print(l2) # (6, 4, 2, 7)

print(list(l1)) # [1, 9, 5, 3]
print(list(l2)) # [6, 4, 2, 7]

# for pair in zip(l1,l2):
#     new_list.append(max(pair))

# print(new_list)