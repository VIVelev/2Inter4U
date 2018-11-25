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
]

with open("./src/static/tfidf.b", mode="rb") as f:
    tf_idf = pickle.load(f)

def preprocess(text):
    data = np.array([text])

    standardize(data)
    remove_noise(data)
    stem(data)
    X = tf_idf.transform(data)

    return X

def summarize_article(text):
    return summarize(text, ratio=0.02)

def get_named_entities(a):
    doc = spacy_nlp(ner_preprocessing(a))
    return [(x.text, x.label_) for x in doc.ents]
