from fastapi import FastAPI
import pickle

# class Item(BaseModel):
#     text: str

# with open("models/model.pkl", "rb") as file:
#     modelo = pickle.load(file)

# with open("models/gnb.pkl", "rb") as file:
#     gnb = pickle.load(file)

# with open("models/tfidf.pkl", "rb") as file:
#     tfidf = pickle.load(file)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
    


# @app.post("/predict/{model}")
# def predict(model: str, item: Item):
#     X = modelo.transform([item.text]).toarray()
#     if model == "logistic_regression":
#         pred = modelo.predict(X)
#     elif model == "naive_bayes":
#         pred = modelo.predict(X)

#     return {"model": model, "text": item.text, "prediction": pred.tolist()}