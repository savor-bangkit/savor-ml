import os
import shutil
import glob

needed_folder = ['FLOUR', 'OIL', 'PASTA', 'CAKE', 'MILK', 'TOMATO_SAUCE', 'CEREAL',
                 'WATER', 'SODA', 'JUICE', 'COFFEE', 'TEA', 'SPICES', 'SUGAR', 'JAM'
                 ]
root = r"C:\xampp1\htdocs\savor-ml"

freiburg_dataset = os.path.join(root, "freiburg_groceries_dataset")

#remove unused folder
for f in os.listdir(freiburg_dataset):
    if f not in needed_folder:
        path = os.path.join(freiburg_dataset, f)
        shutil.rmtree(path)

#rename files to match folder
for folder in os.listdir(freiburg_dataset):
    for count, file in enumerate(os.listdir(os.path.join(freiburg_dataset, folder))):
        dst = f"{folder} {str(count)}.jpg"
        src =f"{freiburg_dataset}\\{folder}\\{file}"  
        dst =f"{freiburg_dataset}\\{folder}\\{dst}"  
        os.rename(src, dst)

#copy to Dataset folder
new_dir = os.path.join(root, "Dataset")
if os.path.exists(new_dir)==False:
    os.mkdir(new_dir)
else: 
    pass
shutil.copytree(freiburg_dataset, new_dir, dirs_exist_ok=True)   

shutil.rmtree(freiburg_dataset)