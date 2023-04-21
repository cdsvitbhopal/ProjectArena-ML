from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import tensorflow as tf
import numpy as np
from keras.models import load_model
import io
import json

with open('C:\\Users\\Admin\\PycharmProjects\\pythonProject\\tokenizer.json') as f:
    data = json.load(f)
    tokenizer = tf.keras.preprocessing.text.tokenizer_from_json(data)

model = load_model('C:\\Users\\Admin\\PycharmProjects\\pythonProject\\model.h5')

word_index = tokenizer.word_index
max_length = 25
word_index["<PAD>"] = 0

import streamlit as st
st.title("Fake News Detection")
def fakenewsdetection():
    user = st.text_area("Enter Any News or news content: ")
    if len(user) < 1:
        st.write("  ")
    else:
        text = user
        test_sentence = np.array([text])

        test_sequence = tokenizer.texts_to_sequences(test_sentence)

        test_padded = tf.keras.preprocessing.sequence.pad_sequences(sequences=test_sequence, value=word_index["<PAD>"],
                                                                    padding="post", maxlen=max_length,
                                                                    truncating='post')

        predictions = model.predict(test_padded)
        predictions = [1 if p > 0.5 else 0 for p in predictions]
        if (predictions[0] == 0):
            st.write("The given news is false.")
        else:
            st.write("The given news is reliable.")
fakenewsdetection()

