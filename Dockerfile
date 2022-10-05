FROM python:3.8

WORKDIR /churn-bank

COPY ..
RUN chmod +x /churn-bank/start.sh

CMD ["sh","-c", "/churn-bank/start.sh && streamlit run streamlit.py --server.port $PORT"]