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

df = load_data(file)

st.markdown("## EDA 및 품목 선정 여정 ")

# st.dataframe(df)

# <품목별 Correlation >
st.subheader("✔ ")
st.markdown("")
tab1, tab2, tab3 = st.tabs(["🧄 마늘","🥔 감자", "🍠 고구마", "🍃 깻잎" ])

# pv1 = df.pivot_table(index="Product" =="마늘", columns="월", values="건수")
st.DataFrame(df)

plt.figure(figsize=(15, 10))
sns.heatmap(pv1, annot=True, fmt=".2f", cmap="flare")
tab1.markdown("**월/요일에 따른 사고 발생 평균**")
tab1.pyplot(plt)


pv2 = df.pivot_table(index="시간대", columns="요일", values="건수")
pv2 = pv2.reindex(columns=list("월화수목금토일"))

plt.figure(figsize=(15, 10))
sns.heatmap(pv2, annot=True, fmt=".2f", cmap="flare")
tab2.markdown("**요일/시간대에 따른 사고 발생 평균**")
tab2.pyplot(plt)


pv3 = df.pivot_table(index="시간대", columns="월", values="건수")

plt.figure(figsize=(15, 10))
sns.heatmap(pv3, annot=True, fmt=".2f", cmap="flare");
tab3.markdown("**월/시간대에 따른 사고 발생 평균**")
tab3.pyplot(plt)




st.markdown("")
st.markdown("---")
st.markdown("")