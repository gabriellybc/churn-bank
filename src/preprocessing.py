from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pandas as pd

def split(df, test_size=0.1, random_state=42):
    X = df.drop(columns=['exited'])
    y = df['exited']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return (X_train, X_test, y_train, y_test)

def encode(df):
    label_encoder = LabelEncoder()
    df['geography'] = label_encoder.fit_transform(df['geography'])
    df['gender'] = label_encoder.fit_transform(df['gender']) 
    df['has_cr_card'] = label_encoder.fit_transform(df['has_cr_card']) 
    df['is_active_member'] = label_encoder.fit_transform(df['is_activemember']) 
    df['exited'] = label_encoder.fit_transform(df['exited'])
    df['age_group'] = label_encoder.fit_transform(df['age_group'])
    df['credit_store_group'] = label_encoder.fit_transform(df['credit_store_group'])
    df['estimated_salary_group'] = label_encoder.fit_transform(df['estimated_salary_group'])
    df['balance_group'] = label_encoder.fit_transform(df['balance_group'])
    return df

def age_group(df):
    age_cat_edges = [0, 20, 40, 60,100]
    df['age_group'] = pd.cut(df['age'], age_cat_edges, labels=['Jovem','Adulto','Meia-Idade','Idoso'])
    return df

def credit_score_group(df):
    credit_store_edges = [200,600,800,10000]
    df['credit_store_group'] = pd.cut(df['credit_score'], credit_store_edges, labels = ['Baixo', 'Regular','Alto'])
    return df

def estimated_salary_group(df):
    estimated_salary_edges = [0, 50000,100000,150000,500000]
    df['estimated_salary_group'] = pd.cut(df['estimated_salary'], estimated_salary_edges, labels = ['Menor que 50.000', '50.000-100.000','100.000-150.000','Maior que 150.000'])
    return df

def balance_group(df):
    balance = [-1,50000,100000,150000,200000,400000]
    df['balance_group'] = pd.cut(df['balance'], balance, labels = ['Menor que 50.000', '50.000-100.000','100.000-150.000','150.000-200.000','Maior que 200.000'])
    return df

def group_by_tracks(df):
    df = age_group(df)
    df = credit_score_group(df)
    df = estimated_salary_group(df)
    df = balance_group(df)
    return df

def preprocess(df):
    df = df.drop(columns=['customer_id', 'surname'])
    df = group_by_group(df)
    df = encode(df)
    X_train, X_test, y_train, y_test = split(df)
    return (X_train, X_test, y_train, y_test)