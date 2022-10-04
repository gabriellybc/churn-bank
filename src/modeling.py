from sklearn.linear_model import LogisticRegression
from skleartn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import f1_score, make_scorer
import numpy as np

def model_generation():
    # logistic_regression = Pipeline([
    #     ('scaler', StandardScaler()),
    #     ('clf', LogisticRegression(random_state=42))
    # ])

    decision_tree = Pipeline([
        ('clf', DecisionTreeClassifier(random_state=42))
    ])

    random_forest = Pipeline([
        ('clf', RandomForestClassifier(random_state=42))
    ])

    models = [
        # logistic_regression,
        decision_tree,
        random_forest
    ]
    return models

def best_model(models, X_train, y_train):
    results = []
    for model in models:
        f1 = cross_val_score(model, X_train, y_train, cv=5, scoring='f1_score').mean()
        results = np.array(results)
        results.append(f1)
        return models[np.argmax(results)]

def model_tuning(model, X_train, y_train):
    f1 = make_scorer(f1_score)
    parameters = {
        'clf__max_depth': [1, 2, 3, 5, 7, 9],
        'clf__min_samples_leaf': [1, 2, 3, 4],
        'clf__min_samples_split': [2, 3, 4, 5]
    }

    grid_search = GridSearchCV(model, parameters, scoring=f1, cv=5)
    grid_search.fit(X_train, y_train)
    return grid_search.best_estimator_

def modeling(X_train, y_train):
    models = model_generation()
    best_model = best_model(models, X_train, y_train)
    best_estimator = model_tuning(best_model, X_train, y_train)
    best = best_estimator.fit(X_train, y_train)
    return best