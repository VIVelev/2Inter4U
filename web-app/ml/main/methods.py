import pickle

from .algo import MyModel
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

__all__ = [
    "predict_emotion",
    "train_recommendation_model",
    "predict_recommendation",
]

sentiment_algo = pickle.load(open("./main/sentiment_algo.pickle", "rb"))

def predict_emotion(X):
    return sentiment_algo.predict(X)[0]

def train_recommendation_model(X_train, y_train):
    model = MyModel(
        BernoulliNB(alpha=1.0),
        BernoulliNB(alpha=1.0),
        LogisticRegression(C=1.0, dual=True),
        DecisionTreeClassifier(max_depth=100),
    )

    model.fit(X_train, y_train)
    return model    

def predict_recommendation(model, X_test):
    return model.predict(X_test)[0]
