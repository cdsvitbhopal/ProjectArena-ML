import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Read the data
news = pd.read_csv('C:\\Users\\Admin\\OneDrive\\Desktop\\Project\\Final.csv')



column_n = ['Unnamed: 0', 'Headline', 'Target']
remove_c = ['Unnamed: 0']
categorical_features = []
target_col = ['Target']
text_f = ['title']
x = np.array(news["title"])
y = np.array(news["Target"])

import nltk
from nltk.corpus import stopwords
import re
from nltk.stem.porter import PorterStemmer
from collections import Counter

ps = PorterStemmer()
wnl = nltk.stem.WordNetLemmatizer()

stop_words = stopwords.words('english')
stopwords_dict = Counter(stop_words)


# Removed unused columns
def remove_unused_c(df, column_n=None):
    if column_n is None:
        column_n = remove_c
    df = df.drop(column_n, axis=1)
    return df


# Impute null values with None
def null_process(feature_df):
    for col in text_f:
        feature_df.loc[feature_df[col].isnull(), col] = "None"
    return feature_df


def clean_dataset(df):
    # remove unused column
    df = remove_unused_c(df)
    #impute null values
    df = null_process(df)
    return df

# Cleaning text from unused characters
def clean_text(text):
    text = str(text).replace(r'http[\w:/\.]+', ' ')  # removing urls
    text = str(text).replace(r'[^\.\w\s]', ' ')  # remove everything but characters and punctuation
    text = str(text).replace('[^a-zA-Z]', ' ')
    text = str(text).replace(r'\s\s+', ' ')
    text = text.lower().strip()
    #text = ' '.join(text)
    return text



## Nltk Preprocessing include:
# Stop words, Stemming and Lemmetization
# For our project we use only Stop word removal
def nltk_preprocess(text):
    text = clean_text(text)
    wordlist = re.sub(r'[^\w\s]', '', text).split()
    # text = ' '.join([word for word in wordlist if word not in stopwords_dict])
    # text = [ps.stem(word) for word in wordlist if not word in stopwords_dict]
    text = ' '.join([wnl.lemmatize(word) for word in wordlist if word not in stopwords_dict])
    return text


# Perform data cleaning on train and test dataset by calling clean_dataset function
df = clean_dataset(news)
# apply preprocessing on headline through apply method by calling the function nltk_preprocess
df["title"] = df.title.apply(nltk_preprocess)

cv = CountVectorizer()
x = cv.fit_transform(x)

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)
model = MultinomialNB()
model.fit(xtrain, ytrain)

import streamlit as st
st.title("Fake News Detection")
def fakenewsdetection():
    user = st.text_area("Enter any news or news content: ")
    if len(user) < 1:
        st.write("  ")
    else:
        sample = user
        data = cv.transform([sample]).toarray()
        a = model.predict(data)
        if ((a)[0]==0):
            st.write("The given news is false.")
        else:
            st.write("The given news is reliable.")
fakenewsdetection()



