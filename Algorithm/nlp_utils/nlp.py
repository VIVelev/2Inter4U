import nltk

__all__ = (
    "standartize",
)

def standartize(df):
    lookup_table = {
        "'ve": "have",
        "'re": "are",
        "'s": "is",
        "n't": "not",
        "'d": "had"
    }
    
    for i in range(len(df)):
        text = df.iloc[i]["text"].lower()
        sents = nltk.sent_tokenize(text)
        
        for j in range(len(sents)):
            words = nltk.word_tokenize(sents[j])
            for k in range(len(words)):
                if words[k] in lookup_table.keys():
                    words[k] = lookup_table[words[k]]
   
            sents[j] = " ".join(words)
        
        text = " ".join(sents)
        df.iloc[i]["text"] = text