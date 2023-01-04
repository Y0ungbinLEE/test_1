import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
# import plotly.express as px
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
import pprint
import koreanize_matplotlib
import altair as alt
from PIL import Image

st.set_page_config(
    page_title="Agriculture",
    page_icon="🌾",
    layout="wide",
)

file = 'AgriMarket.csv'

@st.cache
def load_data(file):
    data = pd.read_csv(file)
    return data

data = load_data(file)

st.dataframe(data)

data_1 = data.loc[data['Product']=='마늘', ['YMD','Price']]
data_1['Y'] = data_1['YMD'].map(lambda x:str(x)[:4])
data_1['M'] = data_1['YMD'].map(lambda x:str(x)[4:6])
data_1 = data_1.drop('YMD', axis=1)

# data_1 = pd.DataFrame(data_1.groupby('M')['Price'].sum())
# data_1m = pd.DataFrame(data_1.groupby('M')['Price'].sum())

st.dataframe(data_1)
# st.dataframe(data_1m)