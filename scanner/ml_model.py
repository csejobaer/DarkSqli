from sklearn.ensemble import IsolationForest

def train_model():
    # fake training data (response length আচরণ)
    X = [[1000], [1020], [980], [995], [1010], [5000]]  

    model = IsolationForest(contamination=0.2)
    model.fit(X)

    return model


def predict_anomaly(model, value):
    pred = model.predict([[value]])
    return pred[0] == -1   # anomaly হলে True
