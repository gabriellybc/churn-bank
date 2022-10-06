from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pandas as pd

def split(df, test_size=0.1, random_state=42):
    X = df.drop(columns=['Exited'])
    y = df['Exited']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return (X_train, X_test, y_train, y_test)

def encode(df):
    label_encoder = LabelEncoder()
    df['Geography'] = label_encoder.fit_transform(df['Geography'])
    df['Gender'] = label_encoder.fit_transform(df['Gender']) 
    df['HasCrCard'] = label_encoder.fit_transform(df['HasCrCard']) 
    df['IsActiveMember'] = label_encoder.fit_transform(df['IsActiveMember']) 
    df['Exited'] = label_encoder.fit_transform(df['Exited'])
    df['AgeGroup'] = label_encoder.fit_transform(df['AgeGroup'])
    df['CreditStoreGroup'] = label_encoder.fit_transform(df['CreditStoreGroup'])
    df['EstimatedSalaryGroup'] = label_encoder.fit_transform(df['EstimatedSalaryGroup'])
    df['BalanceGroup'] = label_encoder.fit_transform(df['BalanceGroup'])
    return df

def age_group(df):
    age_cat_edges = [0, 20, 40, 60,100]
    df['AgeGroup'] = pd.cut(df['Age'], age_cat_edges, labels=['Jovem','Adulto','Meia-Idade','Idoso'])
    return df

def credit_score_group(df):
    credit_store_edges = [200,600,800,10000]
    df['CreditStoreGroup'] = pd.cut(df['CreditScore'], credit_store_edges, labels = ['Baixo', 'Regular','Alto'])
    return df

def estimated_salary_group(df):
    estimated_salary_edges = [0, 50000,100000,150000,500000]
    df['EstimatedSalaryGroup'] = pd.cut(df['EstimatedSalary'], estimated_salary_edges, labels = ['Menor que 50.000', '50.000-100.000','100.000-150.000','Maior que 150.000'])
    return df

def balance_group(df):
    balance = [-1,50000,100000,150000,200000,400000]
    df['BalanceGroup'] = pd.cut(df['Balance'], balance, labels = ['Menor que 50.000', '50.000-100.000','100.000-150.000','150.000-200.000','Maior que 200.000'])
    return df

def group_by_tracks(df):
    df = age_group(df)
    df = credit_score_group(df)
    df = estimated_salary_group(df)
    df = balance_group(df)
    return df

def preprocess(df):
    df = df.drop(columns=['CustomerId', 'Surname'])
    df = group_by_tracks(df)
    df = encode(df)
    X_train, X_test, y_train, y_test = split(df)
    return (X_train, X_test, y_train, y_test)