# readfile
# open function
# read method
# seek method
# tell method
# readline method
# readlines method
# close method


# print(f"cursor position {f.tell()}")
# print(f.read()) # gives data in string form
# print(f.readline(), end='')
# print(f.readline(), end='')
# print(f.readline(), end='')
# print(f"cursor position {f.tell()}")
# print('before seek method')
# f.seek(0)
# print('after seek method')
# print(f"cursor position {f.tell()}")
# print(f.read()) # gives data in string form
# lines = f.readlines()
# print(len(lines))
# for line in lines:
#     print(line, end = '')

f = open('file.txt', 'r') # default mode is r = read

# name , closed
print(f.closed) # data descriptor

f.close()
print(f.closed)