from elasticsearch import Elasticsearch
from datetime import datetime

__all__ = [
    "init_index",
]

def init_index(INDEX_NAME="chatbot"):
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
            "blog" : {
                "properties" : {
                    "title": {"type" : "text"},
                    "text": {"type" : "text"},
                    "date": {"type": "date"}
                }
            }
        },
    }

    print("creating '%s' index..." % (INDEX_NAME))
    res = es.indices.create(index = INDEX_NAME, body = request_body)
    print(" response: '%s'" % (res))

    return es
