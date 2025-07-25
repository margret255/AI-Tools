# -*- coding: utf-8 -*-
"""Untitled26.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JGFw1PY_VMeZk7ndzjYMa2ENBavv1bjd
"""

import spacy
nlp = spacy.load("en_core_web_sm")

reviews = [
    "I love the new Apple iPhone! The camera quality is amazing.",
    "This Samsung charger stopped working after a week. Total waste.",
    "The Sony headphones are super comfortable and sound great.",
    "Terrible experience with this Lenovo laptop. It lags too much.",
    "The Nike shoes fit perfectly and look awesome!"
]

positive_words = ["love", "amazing", "super", "comfortable", "great", "perfectly", "awesome"]
negative_words = ["stopped", "waste", "terrible", "lags", "bad", "poor"]

#preprocessing reviews
for review in reviews:
    doc = nlp(review)

    # Extract named entities
    print("\n📄 Review:", review)
    print("🔍 Named Entities (PRODUCT / ORG):")
    for ent in doc.ents:
        if ent.label_ in ["PRODUCT", "ORG"]:
            print(f" - {ent.text} ({ent.label_})")

    # Simple rule-based sentiment analysis
    sentiment = "Neutral"
    review_lower = review.lower()
    if any(word in review_lower for word in positive_words):
        sentiment = "Positive"
    elif any(word in review_lower for word in negative_words):
        sentiment = "Negative"

    print("🧠 Sentiment:", sentiment)

