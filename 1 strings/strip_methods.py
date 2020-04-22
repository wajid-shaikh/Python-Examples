name = "    Har    shit    "
dots = "..............."
# to remove white spaces we use strip methods
print(name+dots)
print(name.lstrip() + dots) # remove spaces from left side
print(name.rstrip() + dots) # remove spaces from right side
print(name.strip() + dots) # remove spaces from both left and right side
print(name.replace(" ","") + dots) # remove all spaces 
