import pandas as pd

import nltk
from gensim.summarization.summarizer import summarize

import nlp

__all__ = [
    "preprocess",
    "summarize_article",
    "named_entity_recognition",
]


# TODO: Implement TF-IDF
tf_idf = None

def preprocess(text):
    data = pd.DataFrame(
            [[text, "-"], ["-", "-"]],
            columns=["text", "label"]
        )

    nlp.standartize(data)
    nlp.remove_noise(data)
    nlp.stem(data)
    X = tf_idf.transform(data["text"])

    return X

def summarize_article(text):
    summary = summarize(text, ratio=0.02)
    sents = nltk.sent_tokenize(summary)[:5]
    res = ". ".join(sents)
    return res

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
