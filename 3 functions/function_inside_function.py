def greater(a,b):
    if a>b:
        return a
    return b

def new_greater(a,b,c):
    bigger = greater(a,b)
    return greater(bigger , c)

print(new_greater(15,20,9))