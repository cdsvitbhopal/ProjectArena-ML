import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

def transform_text(text):
    """
    Transform a text message by converting it to lowercase, removing stop words, and stemming the words.

    Parameters
    ----------
    text : str
        The text message to transform.

    Returns
    -------
    str
        The transformed text message.
    """

    text = text.lower()
    text = nltk.word_tokenize(text)

    # Remove stop words
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    # Remove punctuation
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    # Stem the words
    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))


st.title("SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):

    # Preprocess the text message
    transformed_sms = transform_text(input_sms)

    # Vectorize the text message
    vector_input = tfidf.transform([transformed_sms])

    # Predict the class of the text message
    result = model.predict(vector_input)[0]

    # Display the results
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
