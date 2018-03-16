import pickle
import pandas as pd
from .nlp import *

__all__ = [
    "preprocess",
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

