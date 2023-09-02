import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB

data = pd.read_csv("Youtube01-Psy.csv")
print(data.sample(5))

data = data[["CONTENT", "CLASS"]]
print(data.sample(5))

data["CLASS"] = data["CLASS"].map({0: "Not Spam",
                                   1: "Spam Comment"})
print(data.sample(5))

x = np.array(data["CONTENT"])
y = np.array(data["CLASS"])

cv = CountVectorizer()
x = cv.fit_transform(x)
xtrain, xtest, ytrain, ytest = train_test_split(x, y, 
                                                test_size=0.2, 
                                                random_state=42)

model = BernoulliNB()
model.fit(xtrain, ytrain)
print(model.score(xtest, ytest))

