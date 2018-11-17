import pandas as pd

__all__ = [
    "text2array",
    "array2df",
    "text2df",
    "DIR"
]

DIR = "/Users/victor/Desktop/OldAndBald/app/data/"

def text2array(file, DIR=DIR, is_yelp=False):
    res = []
    with open(DIR+file) as f:
        sents = f.readlines()
        for sent in sents:
            label, data = sent.split("\t")
            
            if is_yelp:
                res.append([label, data])
            else:
                res.append([data, label])
        
        
    return res

def array2df(array):
    return pd.DataFrame(array, columns=["text", "label"])

def text2df(file): 
    return array2df(text2array(file))