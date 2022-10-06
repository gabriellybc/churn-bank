import pandas as pd

def data_collect():
    df = pd.read_csv(
        'https://raw.githubusercontent.com/gabriellybc/churn-deploy/main/data/Churn_Modelling.csv'
        , index_col='RowNumber'
        , sep=','
        , encoding='UTF-8'
        , header=0
    )
    return df