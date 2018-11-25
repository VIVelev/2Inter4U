import os
import pickle

import nltk
import spacy
import numpy as np
from gensim.summarization.summarizer import summarize

from .preprocessing import standardize, remove_noise, stem, ner_preprocessing
spacy_nlp = spacy.load("en_core_web_sm")

__all__ = [
    "preprocess",
    "summarize_article",
    "get_named_entities",
    "get_sentiment",
]

if os.getcwd().split('/')[-1] == "2Inter4U":
    with open("./src/static/tfidf.b", mode="rb") as f:
        tf_idf = pickle.load(f)
        print("TF-IDF binary loaded successfully.")

    with open("./src/static/logistic.b", mode="rb") as f:
        logistic = pickle.load(f)
        print("Logistic binary loaded successfully.")

else:
    print("TF-IDF && Logistic binary not loaded.")

def preprocess(text):
    return tf_idf.transform(
        stem(remove_noise(standardize(
            np.array([text])
        )))
    )

def summarize_article(text):
    return summarize(text, ratio=0.02)

def get_named_entities(text):
    doc = spacy_nlp(ner_preprocessing(text))
    return [(x.text, x.label_) for x in doc.ents]

def get_sentiment(text):
    return logistic.predict_proba(preprocess(text))
