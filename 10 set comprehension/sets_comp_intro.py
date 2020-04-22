# sets comprehension ---> only one video
# s = {k**2 for k in range(1,11)}
# print(s)

names = ['wajid', 'joe', 'martin']
# first = {names[0] for name in names}
# print(first)

# or

n = set()
for name in names:
    n.add(name[0])
print(n)