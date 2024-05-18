#USED TO RENAME FILES FROM 0_100,1_100,.. TO {FRUIT} 0,{FRUIT} 1,..

# importing the module
import shutil
import os

ls_folder = ["Apple Braeburn", "Apple Crimson Snow", "Apple Golden 1", "Apple Golden 2", "Apple Golden 3", "Apple Granny Smith", "Apple Pink Lady", "Apple Red 1", "Apple Red 2", "Apple Red 3", "Apple Red Delicious", "Apple Red Yellow 1", "Apple Red Yellow 2", 
              "Avocado", "Avocado ripe", 
              "Banana", "Banana Lady Finger", "Banana Red", 
              "Cantaloupe 1", "Cantaloupe 2", 
              "Cauliflower", 
              "Cucumber Ripe", "Cucumber Ripe 2", 
              "Eggplant", 
              "Grape Blue", "Grape Pink", "Grape White", "Grape White 2", "Grape White 3", "Grape White 4", 
              "Guava", 
              "Kiwi",
              "Lemon", "Lemon Meyer", 
              "Limes", 
              "Lychee", 
              "Mango", "Mango Red", 
              "Mangostan", 
              "Onion Red", "Onion Red Peeled", "Onion White", 
              "Orange", 
              "Papaya", 
              "Pear", "Pear 2", "Pear Abate", "Pear Forelle", "Pear Kaiser", "Pear Monster", "Pear Red", "Pear Stone", "Pear Williams", 
              "Pepper Green", "Pepper Orange", "Pepper Red", "Pepper Yellow", 
              "Pineapple", "Pineapple Mini", 
              "Potato Red", "Potato Red Washed", "Potato Sweet", "Potato White", 
              "Rambutan", 
              "Salak", 
              "Strawberry", "Strawberry Wedge", 
              "Tomato 1", "Tomato 2", "Tomato 3", "Tomato 4","Tomato Cherry Red", "Tomato Heart", "Tomato Maroon","Tomato not Ripened", "Tomato Yellow", 
              "Watermelon", 
              "Corn", "Corn Husk"] 

dir = ["Training","Test"]
root = r"C:\xampp1\htdocs\savor-ml\fruits-360-100x100"

# Fetching all the files to directory

for i in dir:
    directory = os.path.join(root, i)
    for folder in ls_folder:
        cur_dir = os.path.join(directory, folder)
        for count, filename in enumerate(os.listdir(cur_dir)):
            dst = f"{folder} {str(count)}.jpg"
            src =f"{cur_dir}\\{filename}"  # foldername/filename, if .py file is outside folder
            dst =f"{cur_dir}\\{dst}"      
        # rename() function will
        # rename all the files
            os.rename(src, dst)