import pickle

__all__ = (
    "predict_emotion",
)

sentiment_algo = pickle.load(open("../Algorithm/main/sentiment_algo.pickle", "rb"))
def predict_emotion(text):
    return "Test"