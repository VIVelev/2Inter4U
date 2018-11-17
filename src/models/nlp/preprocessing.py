import re
import nltk

__all__ = [
    "standartize",
    "remove_punct",
    "remove_noise",
    "lemmatize",
    "stem",
]


def standartize(df):
    lookup_table = {
        "'ve": "have",
        "'re": "are",
        "'s": "is",
        "n't": "not",
        "'d": "had",
        "luv": "love",
        "pls": "please",
        "fck": "fuck",
        "thx": "thanks",
        "np": "no problem",
        "u": "you",
    }
    
    corpus = ['' for _ in range(df.shape[0])]
    i = 0
    for sample in df.values:
        for sent in nltk.sent_tokenize(sample[0].lower()):
            for word in nltk.word_tokenize(sent):

                if word in lookup_table.keys():
                    corpus[i] += lookup_table[word]
                else:
                    corpus[i] += word
                corpus[i] + ''
        i+=1

    df["text"] = corpus


def remove_punct(text):
    punct = ["`", "(\!)", "@", "#", "(\$)", "%", "(\^)", "(\&)", "(\*)", "(\()", "(\))", "-", "(\+)", "=",
            "(\{)", "(\})", "(\[)", "(\])", "(\|)", "(\\\\)",
            ":", ";", "(\")", "(\')",
            ",", "(\.)", "/", "<", ">", "(\?)",
            "(\n)", "(\t)"]
    
    for p in punct:
        text = re.sub(p+"+", "", text)
        
    text = re.sub("(\s)+", " ", text)
    return text


def remove_noise(df):
    stop_words = set(nltk.corpus.stopwords.words("english"))
    stop_words.remove("not")
    
    for i in range(len(df)):
        text = df.iloc[i]["text"].lower()
        sents = nltk.sent_tokenize(text)

        for j in range(len(sents)):
            words = nltk.word_tokenize(sents[j])
            for word in words:
                if word in stop_words:
                    words.remove(word)
                
            sents[j] = " ".join(words)
        
        text = " ".join(sents)
        df.iloc[i]["text"] = remove_punct(text)
        df.iloc[i]["label"] = remove_punct(df.iloc[i]["label"])


def lemmatize(df):
    lemmatizer = nltk.WordNetLemmatizer()
    
    for i in range(len(df)):
        text = df.iloc[i]["text"].lower()
        sents = nltk.sent_tokenize(text)
        
        for j in range(len(sents)):
            words = nltk.word_tokenize(sents[j])
            for k in range(len(words)):
                words[k] = lemmatizer.lemmatize(words[k])
                
            sents[j] = " ".join(words)
        
        text = " ".join(sents)
        df.iloc[i]["text"] = text


def stem(df):
    stemmer = nltk.PorterStemmer()
    
    for i in range(len(df)):
        text = df.iloc[i]["text"].lower()
        sents = nltk.sent_tokenize(text)
        
        for j in range(len(sents)):
            words = nltk.word_tokenize(sents[j])
            for k in range(len(words)):
                words[k] = stemmer.stem(words[k])
                
            sents[j] = " ".join(words)
        
        text = " ".join(sents)
        df.iloc[i]["text"] = text
