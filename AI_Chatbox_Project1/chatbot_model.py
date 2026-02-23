import json
import random
import nltk
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

nltk.download('punkt')

# Load intents
with open('intents.json') as file:
    data = json.load(file)

patterns = []
tags = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        patterns.append(pattern)
        tags.append(intent['tag'])

# Convert text to numbers
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(patterns)

# Train model
model = LogisticRegression()
model.fit(X, tags)


def get_response(user_input):
    X_test = vectorizer.transform([user_input])
    prediction = model.predict(X_test)[0]

    for intent in data['intents']:
        if intent['tag'] == prediction:
            return random.choice(intent['responses'])

    return "I don't understand."