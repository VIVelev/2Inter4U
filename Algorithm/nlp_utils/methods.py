import pickle
import pandas as pd

from .nlp import *
from gensim.summarization.summarizer import summarize


__all__ = [
    "preprocess",
    "summarize_article"
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

