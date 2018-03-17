from elasticsearch import Elasticsearch
from datetime import datetime

# Data source
import wikipedia

__all__ = [
    "es",

    "isLoaded",
    "INDEX_NAME",
    "N_WIKI_PAGES",
    "init_index",
    "load_data",


    "init_liked_articles_index",
    "create_liked_article",
    "LIKED_ARTICLES_INDEX_NAME",
]


es = Elasticsearch()

isLoaded = False
INDEX_NAME = "wikipedia"
N_WIKI_PAGES = 100

LIKED_ARTICLES_INDEX_NAME = "liked_articles"


def init_index(INDEX_NAME=INDEX_NAME, N_WIKI_PAGES=N_WIKI_PAGES):
    global es

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
                    "title": {
                        "type" : "text",
                        # "analyzer": "english"
                    },
                    "content": {
                        "type" : "text",
                        # "analyzer": "english"                        
                    },
                    "date": {
                        "type": "date",
                        # "analyzer": "english"
                    }
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

    pages = [
        *wikipedia.search("Bulgaria"),
        *wikipedia.search("Sofia"),        
        *wikipedia.search("Russia"),
        *wikipedia.search("Moscow")        
    ]

    i = 0
    for page in pages[:N_WIKI_PAGES]:
        doc = {}
        try:
            doc = {
                "title": page,
                "content": wikipedia.page(page).content,
                "date": datetime.now()
            }

            es.index(index=INDEX_NAME, doc_type="article", id=i, body=doc)
            i+=1
        except Exception as e:
            pass

    print("Wikipedia database loaded.\n")


def init_liked_articles_index(INDEX_NAME=LIKED_ARTICLES_INDEX_NAME):
    global es

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
                    "title": {
                        "type" : "text",
                        # "analyzer": "english"
                    },
                    "content": {
                        "type" : "text",
                        # "analyzer": "english"                        
                    },
                    "date": {
                        "type": "date",
                        # "analyzer": "english"
                    }
                }
            }
        },
    }

    print("creating '%s' index..." % (INDEX_NAME))
    res = es.indices.create(index = INDEX_NAME, body = request_body)
    print(" response: '%s'" % (res))

    return es


def create_liked_article(_id, _type="article", INDEX_NAME=LIKED_ARTICLES_INDEX_NAME):
    return {
        "_index": INDEX_NAME,
        "_type": _type,
        "_id": _id
    }
