import pickle
import pandas as pd

import nltk
from gensim.summarization.summarizer import summarize

from .nlp import *


__all__ = [
    "preprocess",
    "summarize_article",
    "summarize_categories",
    "named_entity_recognition",
]

tf_idf = pickle.load(open("./nlp_utils/tf_idf.pickle", "rb"))

def preprocess(text):
    data = pd.DataFrame(
            [[text, "-"], ["-", "-"]],
            columns=["text", "label"]
        )

    standartize(data)
    remove_noise(data)
    stem(data)
    X = tf_idf.transform(data["text"])

    return X

def summarize_article(text):
    summary = summarize(text, ratio=0.02)
    sents = nltk.sent_tokenize(summary)[:50]
    res = ". ".join(sents)
    return res

def summarize_categories(text):
    return summarize(text, ratio=0.1)

def named_entity_recognition(text):
    data = nltk.word_tokenize(text)
    data = nltk.pos_tag(data)
    data = nltk.ne_chunk(data)
    data = list(data)
    
    named_entities = []
    
    for x in data:
        if type(x) is nltk.tree.Tree: # if Named Entity
            named_entities.append(x[0][0])
            
    return named_entities

