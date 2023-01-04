import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
# import plotly.express as px
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
import pprint
import koreanize_matplotlib
import altair as alt
#데이터 로드
url = "https://raw.githubusercontent.com/Y0ungbinLEE/test_1/main/Agri_all.csv"
@st.cache
def load_data(url):
   df = pd.read_csv(url)
   return df

df = load_data(url)


st.header(" 🌾 Agricultural Products Price Prediction")

st.markdown("""       """)

st.markdown("## ✔ 품목별 Modeling")
st.markdown("")

st.markdown("## 🚀품목별 데이터🚀")

product = ['마늘', '감자', '고구마', '깻잎']
choice = st.selectbox('품목을 선택해주세요.', product)

if choice == product[0]:
    st.markdown("## 🧄마늘")
    st.dataframe()


elif choice == product[1]:
    st.markdown("## 🥔감자")
    st.dataframe()


elif choice == product[2]:
    st.markdown("## 🍠고구마")
    st.dataframe()


elif choice == product[3]:
    st.markdown("## 🍃깻잎")
    st.dataframe()

