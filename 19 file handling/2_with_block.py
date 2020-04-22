# f = open('file.txt')
# f.read()
# f.close()

# with block
# context manager
with open('file.txt') as f:  # with block - not require any file close i.e f.close
    data = f.read()
    print(data)

# print(f.closed)