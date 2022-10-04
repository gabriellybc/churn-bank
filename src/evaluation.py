from sklearn.metrics import f1_score

def evaluation(model, X_test, y_test):
    y_pred = model.predict(X_test)
    f1 = f1_score(y_test, y_pred)
    return f1