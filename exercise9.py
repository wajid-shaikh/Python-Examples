# ask a user for name
# Example - Harshit Vashisth
# print count of each words
# output : 
        # H : 1
        # a : 2
        # r : 1
        # s : 3
        # h : 3
        # i : 2
        # t : 2
        #   : 1
        # V : 1
name = input("enter your name = ")
n = len(name)
temp_var = ""
i = 0
while i < n:
    if name[i] not in temp_var:
        temp_var = temp_var + name[i]
        print(f"# {name[i]} : {name.count(name[i])}")
    i = i + 1