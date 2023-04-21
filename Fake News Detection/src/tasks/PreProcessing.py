import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from keras.preprocessing.text import Tokenizer
from collections import Counter
import re
import string
import io
import json
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
nltk.download('stopwords')
nltk.download('punkt')

df = pd.read_csv("Final DataFrame.csv") # loaded csv(comman seperated values) files using pandas library

df.drop(['Unnamed: 0'],axis=1,inplace=True) # dropping unnamed column

def lowercase_text(text): 
    return text.lower()
def remove_num(text): 
    result = re.sub(r'\d+', '', text) 
    return result 
def rem_punct(text): 
    translator = str.maketrans('', '', string.punctuation) 
    return text.translate(translator) 
df["text"] = df["text"].apply(lowercase_text)
df["text"] = df["text"].apply(remove_num)
df["text"] = df["text"].apply(rem_punct)
# removing stop word
stop = set(stopwords.words("english"))
def remove_stopwords(text):
  filtered_words = [word.lower() for word in text.split() if word.lower() not in stop]
  return " ".join(filtered_words)
# removing HTML tags from the string
def remove_html_tags(text):
    pattern = re.compile('<.*?>') # used regular expression
    return pattern.sub(r'', text)
# removing Uniform Resource Locator(URL) from string
def remove_url(text):
    pattern = re.compile(r'https?://\S+|www\.\S+') # used regular expression
    return pattern.sub(r'', text)
# Count unique words
def counter_word(text_col):
    count = Counter()
    for text in text_col.values:
        for word in text.split():
            count[word] += 1
    return count
df["text"] = df["text"].apply(remove_html_tags)
df["text"] = df["text"].apply(remove_url)
counter = counter_word(df.text)
num_unique_words = len(counter)
# Split dataset into training(90%) and validation set(10%)
train_size = int(df.shape[0] * 0.9)
train_df = df[:train_size]
val_df = df[train_size:]
# split text and labels
train_sentences = train_df.text.to_numpy()
train_labels = train_df.Target.to_numpy()
val_sentences = val_df.text.to_numpy()
val_labels = val_df.Target.to_numpy()

# Tokenization
# vectorize a text corpus by turning each text into a sequence of integers i.e assigning each unqiue word(vocabulary) a unqiue number
tokenizer = Tokenizer(num_words=num_unique_words)
tokenizer.fit_on_texts(train_sentences) # fit only to training

# each word has unique index
word_index = tokenizer.word_index # dict- each word as key and value is unique indices

train_sequences = tokenizer.texts_to_sequences(train_sentences)
val_sequences = tokenizer.texts_to_sequences(val_sentences)
max_length = 25
word_index["<PAD>"] = 0

train_padded = tf.keras.preprocessing.sequence.pad_sequences(sequences = train_sequences,value=word_index["<PAD>"],padding="post",maxlen=max_length,truncating='post')
val_padded = tf.keras.preprocessing.sequence.pad_sequences(sequences = val_sequences,value=word_index["<PAD>"],padding="post",maxlen=max_length,truncating='post')
# Saving tokenizer
tokenizer_json = tokenizer.to_json()
with io.open('tokenizer.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(tokenizer_json, ensure_ascii=False))  
