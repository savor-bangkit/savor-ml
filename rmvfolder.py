#REMOVE UNUSED FOLDERS

import os
import shutil


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

dir = ["Training", "Test"]
root = r"C:\xampp1\htdocs\savor-ml\fruits-360-100x100"

for i in dir:
    directory = os.path.join(root, i)
    for filename in os.listdir(directory):
        if filename not in ls_folder:
            rmv_path = os.path.join(directory, filename)
            shutil.rmtree(rmv_path)