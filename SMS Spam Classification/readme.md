# SMS Spam Classifier

This project is a spam classifier that uses a TF-IDF vectorizer and multinomial naive Bayes classifier to classify SMS messages as spam or ham.

## Files

* `spam.csv`: The dataset contains 5572 SMS messages, labeled as spam or ham.
* `spam_detection.ipynb`: The Jupyter notebook that contains the code for the spam classifier.
* `app.py`: The Streamlit app that allows users to classify SMS messages as spam or ham.
* `model.pkl`: The pickled model file.
* `vectorizer.pkl`: The pickled vectorizer file.

## Libraries

* pandas
* numpy
* scikit-learn
* matplotlib
* nltk
* seaborn
* wordcloud
* streamlit

## Process

The spam classifier goes through the following process:

1. Data cleaning: The dataset is cleaned by removing unnecessary columns, duplicate rows, and missing values.
2. EDA: Exploratory data analysis is performed to gain insights into the data.
3. Data preprocessing: The data is preprocessed by converting the text to lowercase, removing stop words, and stemming the words.
4. Modeling: A TF-IDF vectorizer is used to create features from the text data. A multinomial naive Bayes classifier is then used to train the model.
5. Evaluation: The model is evaluated on a test set.

## Usage

To use the spam classifier, you can follow these steps:

1. Clone the repository.
2. Install the dependencies.
3. Run the `app.py` file.
4. Enter an SMS message in the input field.
5. Click the "Classify" button.

The app will then classify the SMS message as spam or ham.

## References

* [SMS Spam Collection](https://archive.ics.uci.edu/ml/datasets/sms+spam)
* [Scikit-learn](https://scikit-learn.org/stable/)
* [Streamlit](https://streamlit.io/)

# By VISHNU PRATAP CHOPRA 