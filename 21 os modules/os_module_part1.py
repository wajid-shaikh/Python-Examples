import os

################ to check current working directory #################

# os.getcwd()  -----> gives current working directory
# print(os.getcwd())  # o/p = D:\python\21 os modules

#####################################################################



################ to create folder ###################################

# os.mkdir('movies')    # ----> to create folder of name movies in current working directory

# to check movies folder already exist or not
# we use 
# print(os.path.exists('movies'))   # return true / false

# example 
# if os.path.exists('movies'):
#     print('already exist')
# else:
#     os.mkdir('movies')

#======= create folder in another directory ======#

#--- 1 method ---#
# os.mkdir(r'F:\python')
#----------------#

#--- 2 method ---#
# to change the directory 
# os.chdir(r'F:\python')
# os.mkdir(r'F:\python')
#----------------#

#=================================================#

####################################################################



################ to create files ###################################

# open('file.txt','a').close()    # to create file 

####################################################################


################ to display all contents in folder #################

# print(os.listdir(r'F:\movies\Hollywood'))

for item in os.listdir():
    path = os.path.join(os.getcwd(), item)
    print(path)

####################################################################