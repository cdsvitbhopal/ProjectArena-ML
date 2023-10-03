# Mushroom Edibility Classification

This project analyzes whether a mushroom is poisonous or edible. The first half involves Elementary Data Analysis followed by Classification using DecisionTreeClassifier and RandomForestClassifier. We then compare the accuracies achieved by both models.

## Dataset

The project utilizes the kaggle dataset [Mushroom Edibility CLassification](https://www.kaggle.com/datasets/devzohaib/mushroom-edibility-classification/). This dataset includes 61069 hypothetical mushrooms with caps based on 173 species (353 mushrooms per species). Each mushroom is identified as definitely edible, definitely poisonous, or of unknown edibility and not recommended (the latter class was combined with the poisonous class). Of the 20 variables, 17 are nominal and 3 are metrical. 

Make sure to download the dataset and specify the file path in the code.

## Requirements

- Python 3.x
- pandas
- matplotlib
- seaborn
- sklearn

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/your_username/Mushroom-Edibility-Classification.git
   ```

2. Navigate to the project directory:

   ```
   cd Mushroom-Edibility-Classification
   ```

3. Install the required dependencies:

   ```
   pip install pandas matplotlib seaborn sklearn
   ```

## Usage

1. Place the dataset file in the project directory.

2. Open the Python script `Mushroom-Edibility-Classification.py` and update the following line with the name of your dataset file:

   ```python
   df = pd.read_csv('Mushroom-Edibility-Classification_dataset.csv')
   ```

3. Run the script in terminal:

   ```
   python Mushroom-Edibility-Classification.py
   ```

4. The script will analyze, visualize various aspects of the dataset and train classication machine learning algorithms.


## Results

RandomForestClassifier performed better on test dataset than DecisionTreeClassifier. The dataset was split into 75% and 25% train and test sets.

