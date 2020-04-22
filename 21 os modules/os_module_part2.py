import os
import shutil

os.chdir(r'D:\python\21 os modules')
# print(os.listdir())
# fileiter = os.walk(r'D:\Angular')
# for curr_path, folder_names, file_names in fileiter:
#     print(f"current path = {curr_path}")
#     print(f"folder names = {folder_names}")
#     print(f"file names = {file_names}")

# os.makedirs('new_folder')

# shutil.rmtree('new_folder')

shutil.copytree('movies', 'new_folder\my_movies')

shutil.copy('file.txt', 'movies')