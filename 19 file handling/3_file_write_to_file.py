# w, a, r+
# w , a = creates a file if not created
# r+    = gives error if file not created



# with open('file1.txt', 'w') as f:
#     f.write(' long live the king\n')

# with open('file1.txt', 'a') as f:
#     f.write(' long live the king\n')

with open('file1.txt', 'r+') as f:
    f.seek(len(f.read()))
    f.write('hie there ...\n')