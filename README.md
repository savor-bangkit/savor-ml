![image](https://github.com/savor-bangkit/savor-ml/assets/67036164/3f425e73-8821-465d-a006-c5ec95c1d4e8)

# SAVOR: Waste Less, Taste More

# About The Model
The SAVOR model is designed to help individuals and organizations reduce food waste by predicting optimal usage and storage times for various food items. By leveraging machine learning, the model analyzes data from various sources to provide recommendations that maximize the freshness and usability of food, thereby minimizing waste. The model can be applied in household settings, restaurants, and food supply chains to enhance sustainability efforts.

# Dataset Sources
[Apple](URL)
[Banana](URL)
[Chicken](URL)
[Cucumber](URL)
[Egg](URL)
[Fish](URL)
[Spinach](URL)


# How to Reproduce on Your Machine
1. **Clone the Repository:**
   ```
   git clone https://github.com/savor-bangkit/savor-ml.git
   cd savor
   ```

2. **Setup Enviroment**
   Ensure your enviroment is properly setup by installing python all the library imported in the jupyter notebook file.
   To install python, check https://www.python.org/downloads/ for guides.
   To install other packages, check https://packaging.python.org/en/latest/tutorials/installing-packages/ for guides.

3. **Data Formatting:**
   Place the dataset file in the same directory as the notebook and Run the data formatting script to prepare the datasets. Remember to change the directory in the notebook accordingly. 
   ```
   jupyter notebook "Step 1 - Data Formatting.ipynb"
   ```

4. **Data Preprocessing:**
   Preprocess the formatted data for model training:
   ```
   jupyter notebook "Step 2 - Data Preprocessing.ipynb"
   ```

5. **Formatting:**
   Format the data for model training:
   ```
   jupyter notebook "Step 3 - YOLO Formatting.ipynb"
   ```

6. **Train the Model and preprocess the data**
   Train the model using the preprocessed data:
   ```
   jupyter notebook "Step 4 - Train Model.ipynb"
   ```



# ML Cohorts

| Name | Bangkit ID |  
|----------|----------|
| Amanda Nurul Izzah | M010D4KX1985 |
| Kausar Meutuwah | M010D4KY2071 |
| Femi Nabila Vielita | M004D4KX1816 |


# Theme
Sustainability, Reducing Food Waste
