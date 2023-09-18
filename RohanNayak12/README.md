# Lung Cancer Detection Model
## Why Choosing Lung Cancer as the project
Lung cancer is the leading cause of cancer death worldwide, responsible for an estimated 1.8 million deaths in 2020.
Early detection and treatment of lung cancer can significantly improve survival rates.
Working on lung cancer related projects can help us to improve our understanding of this disease and develop new and better ways to prevent, diagnose, and treat it.
It can also help to raise awareness of lung cancer and reduce the stigma associated with the disease.
## Developing Model
The Model was built using Scikit Learn a popular Machine Learning Library with Python.
For Data Scaling or Normalization Keras API provided by TensorFlow another popular library of Python has been used.
For Visualization Seaborn and Matplotlib Library by Python where Used.
For Scientific computation numpy and pandas were preffered choice.
Dataset was obtained from kaggle at https://www.kaggle.com/datasets/mysarahmadbhat/lung-cancer .
Prefered Model was Regression since it is supervised model and can be highly useful for early and accurate detection of Lung Cancer.
## Usage Guide
Model can be utilised in two ways either by using it on Colab or running it on local machine.
For local machine few steps would be required:
  1-> Install python by downloading it from the official website for free
  2-> Install matplotlib by "pip install matplotlib" 
  3-> Install seaborn by "pip install seaborn"
  4-> Install scikit-learn by "pip install scikit-learn"
  5-> Install keras by "pip install keras"
  6-> Install numpy by "pip install numpy"
  7-> Install pandas by "pip install pandas"
Then simply open the Jupyter Notebook and input your symptoms in Lung_Cancer_Prediction model in 2D array format.
You will then get the results based on your symptoms. 
## Training 
The Model was trained on with 75:25 ratio where 75% of dataset was used to train model and rest 25% was used to test model.
## Results
The Model achieved a score of 90.5% on train set which was a good accuracy for dataset of this scale.