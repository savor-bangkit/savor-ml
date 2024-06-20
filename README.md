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

2. **Install Dependencies:**
   Ensure you have Python installed. Then, install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. **Download Datasets:**
   Download the datasets from the provided sources and place them in the `data` directory within the project folder.

4. **Data Formatting:**
   Run the data formatting script to prepare the datasets:
   ```
   jupyter notebook "Step 1 - Data Formatting.ipynb"
   ```

5. **Data Preprocessing:**
   Preprocess the formatted data for model training:
   ```
   jupyter notebook "Step 2 - Data Preprocessing.ipynb"
   ```

6. **YOLO Formatting:**
   Format the data for YOLO model training:
   ```
   jupyter notebook "Step 3 - YOLO Formatting.ipynb"
   ```

7. **Train the Model:**
   Train the YOLO model using the preprocessed data:
   ```
   jupyter notebook "Step 4 - Train Model.ipynb"
   ```

8. **Run Predictions:**
   Use the trained YOLO model to make predictions:
   ```
   python predict.py --input your_input_file.csv --output your_output_file.csv
   ```


# ML Cohorts

| Name | Bangkit ID |  
|----------|----------|
| Amanda Nurul Izzah | M010D4KX1985 |
| Kausar Meutuwah | M010D4KY2071 |
| Femi Nabila Vielita | M004D4KX1816 |


# Theme
Sustainability, Reducing Food Waste
