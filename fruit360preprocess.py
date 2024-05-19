#USED TO RENAME FILES FROM 0_100,1_100,.. TO {FRUIT} 0 0,{FRUIT} 0 1,..

# importing the module
import os
import glob
import shutil

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

dir = ["Training","Test"]
root = r"C:\xampp1\htdocs\savor-ml"
fruit_dataset = os.path.join(root, "fruits-360-100x100")
needed_path = []

for i in dir:
    directory = os.path.join(fruit_dataset, i)

    #remove unused folder
    #add path to needed_path
    for folder in ls_folder:
        for item in glob.iglob(f"{directory}\{folder}*"):
            if item:
                needed_path.append(item)
            
    #remove folder thats not in needed_path
    for f in os.listdir(directory):
        path = os.path.join(directory, f)
        if path not in needed_path:
            shutil.rmtree(path)

    #rename files to match folder
    for folder in ls_folder:
        for filename in glob.iglob(f"{directory}\{folder}*"):
            for count, file in enumerate(os.listdir(filename)):
                if i=="Training":
                    dst = f"{folder} 0 {str(count)}.jpg"  #add 0 to Training files to avoid duplicates with Test files
                else:
                    dst = f"{folder} 1 {str(count)}.jpg"

                src =f"{filename}\\{file}"  
                dst =f"{filename}\\{dst}"  

                os.rename(src, dst)

    #move to Dataset folder
    #create Dataset folder if it doesnt exist
    new_dir = os.path.join(root, "Dataset")
    if os.path.exists(new_dir)==False:
        os.mkdir(new_dir)
    else: 
        pass

    #copy file to sub folder {fruit} and create if it doesnt exist
    for folder in ls_folder:
        for filename in glob.iglob(f"{directory}\{folder}*"):
            if os.path.exists(os.path.join(new_dir, folder))==False:
                os.mkdir(os.path.join(new_dir, folder))
                shutil.copytree(filename, os.path.join(new_dir, folder), dirs_exist_ok=True) 
            else:
                shutil.copytree(filename, os.path.join(new_dir, folder), dirs_exist_ok=True) 

#if error here, check if all files are copied and remove manually
shutil.rmtree(fruit_dataset)
