import nltk
import spacy
import pandas as pd
from gensim.summarization.summarizer import summarize

import nlp
spacy_nlp = spacy.load("en_core_web_sm")

__all__ = [
    "preprocess",
    "summarize_article",
    "get_named_entities",
]


# TODO: Implement TF-IDF
tf_idf = None

def preprocess(text):
    data = pd.DataFrame(
            [[text, "-"], ["-", "-"]],
            columns=["text", "label"]
        )

    nlp.standardize(data)
    nlp.remove_noise(data)
    nlp.stem(data)
    X = tf_idf.transform(data["text"])

    return X

def summarize_article(text):
    return summarize(text, ratio=0.02)

def get_named_entities(a):
    doc = spacy_nlp(nlp.ner_preprocessing(a))
    return [(x.text, x.label_) for x in doc.ents]
