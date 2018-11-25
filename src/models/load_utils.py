import pandas as pd

__all__ = [
    "text2array",
    "array2df",
    "text2df",
]


def text2array(file):
    res = []
    with open(file) as f:
        for sent in f.readlines():
            text, label = sent.split("\t")
            res.append([text, label[0]])
        
    return res

def array2df(array):
    return pd.DataFrame(array, columns=["text", "label"])

def text2df(file): 
    return array2df(text2array(file))
