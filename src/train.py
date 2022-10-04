from data_collect import data_collect
from eda import eda
from preprocessing import preprocess
from modeling import modeling
from evaluation import evaluation

import pickle

if __name__ == "__main__":
    df = data_collect()
    df.to_csv('data/raw_data.csv', index=False)

    desc, corr = eda(df)
    desc.to_csv('data/describe.csv', index=False)
    corr.savefig('plots/correlation.png')

    X_train, X_test, y_train, y_test = preprocess(df)
    X_train.to_csv('data/X_train.csv', index=False)
    X_test.to_csv('data/X_test.csv', index=False)
    y_train.to_csv('data/y_train.csv', index=False)
    y_test.to_csv('data/y_test.csv', index=False)

    model = modeling(X_train, y_train)
    pickle.dump(model, open('models/model.pkl', 'wb'))

    print(model)

    f1 = evaluation(model, X_test, y_test)
    print('F1 Score:', f1)
