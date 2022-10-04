import pandas as pd

def data_collect():
    df = pd.read_csv(
        'https://raw.githubusercontent.com/gabriellybc/churn-deploy/main/data/Churn_Modelling.csv'
        , index_col='RowNumber'
        , sep=','
        , encoding='UTF-8'
        , header=0
        , names=['row_number','customer_id','surname','credit_score','geography','gender','age','tenure','balance','num_of_products','has_cr_card','is_active_member','estimated_salary','exited']
        , dtype={'customer_id': 'int64', 'credit_score': 'int64','gender': 'category', 'age': 'int64', 'tenure': 'int64', 'balance': 'float64', 'num_of_products': 'int64', 'has_cr_card': 'category', 'is_active_member': 'category', 'estimated_salary': 'float64', 'exited': 'category'}  
    )
    return df