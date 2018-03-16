import pickle
import pandas as pd
import nltk

from .nlp import *
from gensim.summarization.summarizer import summarize


__all__ = [
    "preprocess",
    "summarize_article"
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
    return summarize(summarize(summarize(text)))

def named_entity_recognition(text):
    data = nltk.word_tokenize(text)
    data = nltk.pos_tag(data)
    data = nltk.ne_chunk(data)
    data = list(data)
    
    final = []
    
    for x in data:
        if type(x) is nltk.tree.Tree:
            final.append(x[0][0])
            
    return final

