from unittest import result
import streamlit as st
import requests
import json
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from joblib import load
# import os

st.set_page_config(
    page_title="Churn em Banco",
    page_icon="🏦",
    layout="centered",
    initial_sidebar_state="expanded",
    # menu_items={
    #     'Get Help': 'https://www.extremelycoolapp.com/help',
    #     'Report a bug': "https://www.extremelycoolapp.com/bug",
    #     'About': "# This is a header. This is an *extremely* cool app!"
    # }
)

st.title("Churn em Banco")

st.write("## Classificação de clientes")

st.write("### Modelo de Machine Learning")

st.write("#### Por: [Gabrielly Cariman](https://www.linkedin.com/in/gabrielly-barcelos-cariman/), [Maria Isabel Almeida](https://www.linkedin.com/in/maria-isabel-oliveira-04975a15a), [Rafaela Jessica Calefe](https://www.linkedin.com/in/rafaela-calefe-006704199)")
st.write("#### Data: 06/10/2022")

st.write("### Introdução")

st.write("Esse projeto tem como objetivo criar um modelo de Machine Learning para prever se um cliente irá deixar de usar os produtos do nosso banco.")
st.write("Para isso, utilizaremos um dataset de clientes de um banco fictício, com informações como: idade, sexo, renda, se possui cartão de crédito, se é um cliente ativo, etc.")

st.write("### Descrição dos dados")

st.write("Os dados foram retirados do [Kaggle](https://www.kaggle.com/datasets/shantanudhakadd/bank-customer-churn-prediction?resource=download).")

st.write("### Modelo de Machine Learning")

st.write("O modelo de Machine Learning utilizado foi a Árvore de Decisão.")

st.write("### Métricas")

st.write("A métrica utilizada foi o [F1 Score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html).")

st.write("### Resultados")

st.write("O modelo obteve um F1 Score de 0.66.")

st.write("### Código")

st.write("O código desse projeto está no [GitHub](https://github.com/gabriellybc/churn-bank).")

st.markdown("---")

st.write("Para saber mais sobre o projeto, acesse o [Medium](https://medium.com/@rafajcalefe/por-gabrielly-cariman-maria-isabel-almeida-e-rafaela-jessica-calefe-1285771854fc).")


# MODEL_URL = F'http://localhost:8000/predict'

# def predict_results(url, modelo, sentence):
#     result = requests.post(f"{url}/{modelo}", json={"text": sentence})
#     st.write('O resultado do modelo é: ', json.loads(result.text)["prediction"][0])

# with st.form("my_ml"):
#     sentence = st.text_input("Texto para classificação")
#     model = st.radio(
#         "Escolha o modelo",
#         ("regressão logistica", "sentiment"))
#     predict = st.form_submit_button("Predict")

# if predict and modelo == 'Regressão Logística':
#     predict_results(MODEL_URL, "logistic_regression", sentence)


# st.title("Prevendo o Titanic :passenger_ship: :passenger_ship:")






# model = load("titanic.joblib")

# train = pd.read_csv("train.csv")
# train = train[["Pclass", "Sex", "Age", "Survived"]]
# x_train = train.drop(["Survived"], axis=1)
# y_train = train["Survived"]

# teste = pd.read_csv("teste.csv")
# x_test = teste.drop(["Survived"], axis=1)
# y_test = teste["Survived"]


# score_train = model.score(x_train, y_train)
# score_test = model.score(x_test, y_test)

# st.header("Vendo nossos scores")

# st.slider("Train Score:", min_value=0.0, max_value=1.0, value=float(0.8756))
# st.slider("Test Score:", min_value=0.0, max_value=1.0, value=float(0.987564213))

# st.markdown("---")

# # st.dataframe(train.head())

# st.markdown("---")

# with st.form("predict_data"):
#     st.header("Predição de dados do Titanic!")
#     gender = st.selectbox("Gênero", ["Masculino", "Feminino"])
#     age = st.slider("Idade", 0, 100, value=70)
#     class_ = st.radio("Qual classe?", options=["1ª", "2ª", "3ª"])
#     st.form_submit_button("Prever!")

# gender = "male" if gender == "Masculino" else "female"
# class_ = int(class_[0])

# data = pd.DataFrame({"Pclass": class_, "Sex": gender, "Age": age}, index=[0])


# prediction = model.predict(data)
# prob = model.predict_proba(data)


# if prediction == 1:
#     st.header("Você sobrevive!!")
#     st.balloons()
# else:
#     st.header("Você não sobrevive ☹️")


# st.markdown("---")
# st.table(data)
# prediction[0]
# prob
