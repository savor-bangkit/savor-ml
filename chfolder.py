#USED TO MERGE FOLDERS OF DIFFERENT VARIETY

import os
import shutil
import glob

ls_folder = ["Apple", 
             "Avocado", 
             "Banana", 
             "Cantaloupe", 
             "Cauliflower", 
             "Cucumber", 
             "Corn",
             "Eggplant", 
             "Grape", 
             "Guava", 
             "Kiwi", 
             "Lemon", 
             "Limes", 
             "Lychee", 
             "Mango", 
             "Mangostan",
             "Onion", 
             "Orange", 
             "Papaya", 
             "Pear", 
             "Pepper", 
             "Pineapple", 
             "Potato", 
             "Rambutan",
             "Salak", 
             "Strawberry", 
             "Tomato", 
             "Watermelon"
             ]

dir = ["Training", "Test"]
root = r"C:\xampp1\htdocs\savor-ml\fruits-360-100x100"
ls_newdir = []

# Copy fruit varieties to new folder
for i in dir:
    directory = os.path.join(root, i)
    for folder in ls_folder:
        new_dir = os.path.join(directory, folder+"s")
        os.mkdir(new_dir)
        ls_newdir.append(new_dir)
        for filename in glob.iglob(f"{directory}\{folder}*"):
            shutil.copytree(filename, new_dir, dirs_exist_ok=True)

print(ls_newdir)

#remove old folders
new_lsfolder = [fruit +"s" for fruit in ls_folder]

for i in dir:
    directory = os.path.join(root, i)
    for filename in os.listdir(directory):
        if filename not in new_lsfolder:
            rmv_path = os.path.join(directory, filename)
            shutil.rmtree(rmv_path)


# #move all to parent dir
# source = root
# destination = os.path.dirname(root)

# # code to move the files from sub-folder to main folder. 
# files = os.listdir(source) 
# for file in files: 
#     file_name = os.path.join(source, file) 
#     shutil.move(file_name, destination) 
# print("Files Moved")