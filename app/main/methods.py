import pickle

__all__ = [
    "predict_emotion",
]

sentiment_algo = pickle.load(open("./main/sentiment_algo.pickle", "rb"))

def predict_emotion(X):
    return sentiment_algo.predict(X)[0]
