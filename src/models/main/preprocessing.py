import re
import nltk
import numpy as np

__all__ = [
    "standardize",
    "remove_noise",
    "lemmatize",
    "stem",
    "ner_preprocessing",
]


def standardize(data):
    lookup_table = {
        "'ve": "have",
        "'re": "are",
        "'s": "is",
        "n't": "not",
        "'d": "had",
        "luv": "love",
        "pls": "please",
        "thx": "thanks",
        "np": "no problem",
        "u": "you",
    }
    
    corpus = ['' for _ in range(data.shape[0])]
    i = 0
    
    for sample in data:
        for word in nltk.word_tokenize(sample.lower()):
            if word in lookup_table.keys():
                corpus[i] += lookup_table[word]
            else:
                corpus[i] += word
            corpus[i] += ' '

        i+=1

    return np.array(corpus)


def _remove_punct(text):
    punct = ["`", r"\!", "@", "#", r"\$", "%", r"\^", r"\&",
            r"\*", r"\(", r"\)", "-", r"\+", "=",
            r"\{", r"\}", r"\[", r"\]", r"\|", r"\\",
            ":", ";", "\"", "'",
            ",", r"\.", "/", "<", ">", r"\?",
            "\n", "\t"]
    
    for p in punct:
        text = re.sub(p+"+", '', text)
        
    return text


def remove_noise(data):
    stop_words = set(nltk.corpus.stopwords.words("english"))
    stop_words.remove("not")
    
    corpus = ['' for _ in range(data.shape[0])]
    i = 0

    for sample in data:
        for word in nltk.word_tokenize(sample.lower()):
            if word not in stop_words:
                corpus[i] += word + ' '
            
        corpus[i] = _remove_punct(corpus[i])
        i+=1

    return np.array(corpus)


def lemmatize(data):
    lemmatizer = nltk.WordNetLemmatizer()
    
    corpus = ['' for _ in range(data.shape[0])]
    i = 0

    for sample in data:
        for word in nltk.word_tokenize(sample.lower()):
            corpus[i] += lemmatizer.lemmatize(word) + ' '
        i+=1

    return np.array(corpus)


def stem(data):
    stemmer = nltk.PorterStemmer()
    
    corpus = ['' for _ in range(data.shape[0])]
    i = 0

    for sample in data:
        for word in nltk.word_tokenize(sample.lower()):
            corpus[i] += stemmer.stem(word) + ' '
        i+=1

    return np.array(corpus)


def ner_preprocessing(text):
    tokens = nltk.word_tokenize(text)
    prepositions = ["about", "in"]
    
    for prep in prepositions:
        idxs = [i for i, x in enumerate(tokens) if x == prep]
        for i in idxs:
            if i+1 < len(tokens) and tokens[i+1] not in prepositions:
                tokens[i+1] = tokens[i+1][0].upper() + tokens[i+1][1:]

    return ' '.join(tokens)
