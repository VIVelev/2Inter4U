from elasticsearch import Elasticsearch
from datetime import datetime

# Data source
import wikipedia

__all__ = [
    "isLoaded",
    "init_index",
    "load_data",
    "INDEX_NAME",
    "N_WIKI_PAGES",
]

isLoaded = False
INDEX_NAME = "chatbot"
N_WIKI_PAGES = 1000

def init_index(INDEX_NAME=INDEX_NAME, N_WIKI_PAGES=N_WIKI_PAGES):
    es = Elasticsearch()

    if es.indices.exists(INDEX_NAME):
        print("deleting '%s' index..." % (INDEX_NAME))
        res = es.indices.delete(index = INDEX_NAME)
        print(" response: '%s'" % (res))

    request_body = {
        "settings" : {
            "number_of_shards" : 1,
            "analysis": {
                "filter": {
                    "english_stop": {
                        "type": "stop",
                        "stopwords": "_english_" 
                    },
                    "english_keywords": {
                        "type": "keyword_marker",
                        "keywords": ["example"] 
                    },
                    "english_stemmer": {
                        "type": "stemmer",
                        "language": "english"
                    },
                    "english_possessive_stemmer": {
                        "type": "stemmer",
                        "language": "possessive_english"
                    }
                },
                "analyzer": {
                    "english": {
                        "tokenizer":  "standard",
                        "filter": [
                            "english_possessive_stemmer",
                            "lowercase",
                            "english_stop",
                            "english_keywords",
                            "english_stemmer"
                        ]
                    }
                }
            }
        },
        "mappings" : {
            "article" : {
                "properties" : {
                    "title": {"type" : "text"},
                    "content": {"type" : "text"},
                    "date": {"type": "date"}
                }
            }
        },
    }

    print("creating '%s' index..." % (INDEX_NAME))
    res = es.indices.create(index = INDEX_NAME, body = request_body)
    print(" response: '%s'" % (res))

    load_data(es, n_wiki_pages=N_WIKI_PAGES)

    global isLoaded
    isLoaded = True
    return es


def load_data(es, n_wiki_pages):
    print("\nLoading wikipedia database...")

    for page in wikipedia.random(pages=n_wiki_pages):
        doc = {}
        try:
            doc = {
                "title": page,
                "content": wikipedia.page(page).content,
                "date": datetime.now()
            }

            es.index(index=INDEX_NAME, doc_type="article", id=i, body=doc)
        except Exception as e:
            pass

    print("Wikipedia database loaded.")
