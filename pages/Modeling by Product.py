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


st.header(" 🌾 Agricultural Products Price Prediction")

st.markdown("""       """)

st.markdown("## ✔ 품목별 Modeling")
st.markdown("")

product = ['마늘', '감자', '고구마', '깻잎']
choice = st.selectbox('품목을 선택해주세요.', product)

if choice == product[0]:
    st.markdown("## 🧄 마늘")
    st.markdown("")
    st.markdown("### ARIMA Model")
    image = Image.open('pages/images/modelimage/g-arima.png')
    st.image(image)
    image = Image.open('pages/images/modelimage/g-arima-result.png')
    st.image(image)
    st.markdown("")
    
    st.markdown("### SARIMA X Model")
    
    st.markdown("#### PPI CPI 제외하고 학습")
    image = Image.open('pages/images/modelimage/g-sarimax-woppicpi.png')
    st.image(image)
    image = Image.open('pages/images/modelimage/g-arima-result.png')
    st.image(image)
    st.markdown("")
    
    st.markdown("#### PPI CPI로만 학습")
    image = Image.open('pages/images/modelimage/g-sarimax-wppicpi.png')
    st.image(image)
    image = Image.open('pages/images/modelimage/g-sarimax-wppicpi-result.png')
    st.image(image)
    st.markdown("")
    
    st.markdown("#### 모든 Feature로 학습")
    image = Image.open('pages/images/modelimage/g-sarimax-wallfeatures.png')
    st.image(image)
    image = Image.open('pages/images/modelimage/g-sarimax-wallfeatures-result.png')
    st.image(image)
    st.markdown("")
 
    st.markdown("### Prophet Model")
    image = Image.open('pages/images/modelimage/g-prophet-m.png')
    st.image(image)



elif choice == product[1]:
    st.markdown("## 🥔 감자")
    st.markdown("")
    st.markdown("### ARIMA Model")
    image = Image.open('pages/images/modelimage/p-arima.png')
    st.image(image)
    image = Image.open('pages/images/modelimage/p-arima-result.png')
    st.image(image)
    st.markdown("")
    
    st.markdown("### SARIMA X Model")
    
    st.markdown("#### PPI CPI 제외하고 학습")
    image = Image.open('pages/images/modelimage/p-sarix-wopplcpi.png')
    st.image(image)
    image = Image.open('pages/images/modelimage/p-sarix-wopplcpi-result.png')
    st.image(image)
    st.markdown("")
    
    st.markdown("#### PPI CPI로만 학습")
    image = Image.open('pages/images/modelimage/p-sarix-wppicpi.png')
    st.image(image)
    image = Image.open('pages/images/modelimage/p-sarix-wppicpi-result.png.png')
    st.image(image)
    st.markdown("")
    
    st.markdown("#### 모든 Feature로 학습")
    image = Image.open('pages/images/modelimage/p-sarix-wallfeatures.png')
    st.image(image)
    image = Image.open('pages/images/modelimage/p-sarix-wallfeatures-result.png')
    st.image(image)
    st.markdown("")
 
    st.markdown("### Prophet Model")
    image = Image.open('pages/images/modelimage/p-prophet-m.png')
    st.image(image)


elif choice == product[2]:
    st.markdown("## 🍠 고구마")
    st.markdown("")
    st.markdown("### ARIMA Model")
    image = Image.open('pages/images/modelimage/sp-ari.png')
    st.image(image)
    image = Image.open('pages/images/modelimage/sp-ari-result.png')
    st.image(image)
    st.markdown("")
    st.markdown("### SARIMA  Model")
    image = Image.open('pages/images/modelimage/sp-sarima.png')
    st.image(image)
    image = Image.open('pages/images/modelimage/sp-sarima-result.png')
    st.image(image)
    st.markdown("")
    
    st.markdown("### SARIMA X Model")
    
    st.markdown("#### PPI CPI 제외하고 학습")
    image = Image.open('pages/images/modelimage/sp-sarimax-woppicpi.png')
    st.image(image)
    image = Image.open('pages/images/modelimage/sp-arima-result.png')
    st.image(image)
    st.markdown("")
    
    st.markdown("#### PPI CPI로만 학습")
    image = Image.open('pages/images/modelimage/sp-sarimax-woppicpi.png')
    st.image(image)
    image = Image.open('pages/images/modelimage/sp-arima-result.png')
    st.image(image)
    st.markdown("")
    
    st.markdown("#### 모든 Feature로 학습")
    image = Image.open('pages/images/modelimage/sp-sarimax-woppicpi.png')
    st.image(image)
    image = Image.open('pages/images/modelimage/sp-arima-result.png')
    st.image(image)
    st.markdown("")
 
    st.markdown("### Prophet Model")
    image = Image.open('pages/images/modelimage/s-prophet-m.png')
    st.image(image)



elif choice == product[3]:
    st.markdown("## 🍃 깻잎")
    st.markdown("")
    st.markdown("### ARIMA Model")
    image = Image.open('pages/images/modelimage/k-arima.png')
    st.image(image)
    image = Image.open('pages/images/modelimage/k-arima-result.png')
    st.image(image)
    st.markdown("")
    
    st.markdown("### SARIMA X Model")
    
    st.markdown("#### PPI CPI 제외하고 학습")
    image = Image.open('pages/images/modelimage/k-sarimax-woppicpi.png')
    st.image(image)
    image = Image.open('pages/images/modelimage/k-arima-result.png')
    st.image(image)
    st.markdown("")
    
    st.markdown("#### CPI로만 학습 (PPI값이 존재하지 않음)")
    image = Image.open('pages/images/modelimage/k-sarimax-wppicpi.png')
    st.image(image)
    image = Image.open('pages/images/modelimage/k-sarimax-wppicpi-result.png')
    st.image(image)
    st.markdown("")
    
    st.markdown("#### 모든 Feature로 학습")
    image = Image.open('pages/images/modelimage/k-sarimax-wallfeatures.png')
    st.image(image)
    image = Image.open('pages/images/modelimage/k-sarimax-wallfeatures-result.png')
    st.image(image)
    st.markdown("")
 
    st.markdown("### Prophet Model")
    image = Image.open('pages/images/modelimage/l-prophet-m.png')
    st.image(image)