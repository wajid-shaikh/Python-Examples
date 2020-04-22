# dictionary comprehension = DC
# square = {1:1, 2:4, 3:9}

# normal method
# square = {}
# for i in range(1,5):
#     square[i] = i**2
# print(square)

# or

# DC method

# square = {f"square of {i} is":i**2 for i in range(1,11)}
# print(square)
# for key,value in square.items():
#     print(f"{key} : {value}")

string = "harshit"
# word_count = {char:string.count(char) for char in string}
# print(word_count)
# word_count = {}
# for char in string:
#     word_count[char] = string.count(char)
# print(word_count)