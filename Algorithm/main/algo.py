__all__ = [
    "MyModel",
]

class MyModel(object):

    def __init__(self, model, *args):
        self.model = model
        self.algos = args


    def parse2int(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = 0


    def fit(self, X, y):
        features = []

        for algo in self.algos:
            algo.fit(X, y)

        for algo in self.algos:
            features.append(algo.predict(X))

        features = np.transpose(features)
        #all_features = pd.DataFrame(columns=["text", *[i for i in range(len(self.algos))]])

        #for i in range(len(features)):
        #    all_features = all_features.append(
        #        pd.DataFrame([[X[i], *features[i]]], columns=["text", *[i for i in range(len(self.algos))]])
        #    )

        self.model.fit(features, y)
        return self


    def predict(self, X):
        features = []

        for algo in self.algos:
            features.append(algo.predict(X))

        features = np.transpose(features)
        #all_features = pd.DataFrame(columns=["text", *[i for i in range(len(self.algos))]])
        
        #for i in range(len(features)):
        #    all_features = all_features.append(
        #        pd.DataFrame([[X[i], *features[i]]], columns=["text", *[i for i in range(len(self.algos))]])
        #    )

        return self.model.predict(features)


    def predict_proba(self, X):
        features = []

        for algo in self.algos:
            if type(algo) is LogisticRegression:
                # print(algo)
                features.append(algo.predict_proba(X))

        return features
