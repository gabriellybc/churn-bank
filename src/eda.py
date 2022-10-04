import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px

def describe(df):
    return df.describe()

def correlation(df):
    fig, ax = plt.subplots(figsize=(10,10))
    sns.heatmap(df.corr(), annot=True, colormap="Blues", ax=ax)
    return fig

def eda(df):
    desc = describe(df)
    corr = correlation(df)
    return (desc, corr)