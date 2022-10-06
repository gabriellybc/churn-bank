from fastapi import FastAPI
import pickle
from pydantic import BaseModel

# class Item(BaseModel):
#     text: str

# with open("models/model.pkl", "rb") as file:
#     modelo = pickle.load(file)

# with open("models/gnb.pkl", "rb") as file:
#     gnb = pickle.load(file)

# with open("models/tfidf.pkl", "rb") as file:
#     tfidf = pickle.load(file)

# app = FastAPI()

# @app.post("/predict/{model}")
# def predict(model: str, item: Item):
#     X = modelo.transform([item.text]).toarray()
#     if model == "logistic_regression":
#         pred = modelo.predict(X)
#     elif model == "naive_bayes":
#         pred = modelo.predict(X)

#     return {"model": model, "text": item.text, "prediction": pred.tolist()}