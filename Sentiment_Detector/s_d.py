import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load the IMDb movie reviews dataset
data = pd.read_csv('imdb_dataset.csv')

# Split the dataset into training and testing sets
train_data, test_data, train_labels, test_labels = train_test_split(data['review'], data['sentiment'], test_size=0.2, random_state=42)

# Initialize CountVectorizer to convert text into numerical features
vectorizer = CountVectorizer()

# Fit the vectorizer on the training data and transform the training data
train_features = vectorizer.fit_transform(train_data)

# Transform the testing data using the fitted vectorizer
test_features = vectorizer.transform(test_data)

# Initialize and train a logistic regression model
model = LogisticRegression()
model.fit(train_features, train_labels)

# Make predictions on the testing data
predictions = model.predict(test_features)

# Calculate accuracy score
accuracy = accuracy_score(test_labels, predictions)
print(f"Accuracy: {accuracy}")

# Test the model on new data
new_reviews = ["This movie was fantastic!", "I didn't like the acting in this film."]
new_features = vectorizer.transform(new_reviews)
new_predictions = model.predict(new_features)

for review, prediction in zip(new_reviews, new_predictions):
    print(f"Review: {review}")
    print(f"Sentiment: {'Positive' if prediction == 1 else 'Negative'}\n")
