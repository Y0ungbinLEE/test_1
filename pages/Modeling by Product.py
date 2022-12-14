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
from PIL import Image

st.header(" πΎ Agricultural Products Price Prediction")

st.markdown("""       """)

st.markdown("## β νλͺ©λ³ Modeling")
st.markdown("")

product = ['λ§λ', 'κ°μ', 'κ³ κ΅¬λ§', 'κΉ»μ']
choice = st.selectbox('νλͺ©μ μ νν΄μ£ΌμΈμ.', product)

if choice == product[0]:
    st.markdown("## π§ λ§λ")
    st.markdown("")
    st.markdown("### π ARIMA Model")
    image = Image.open('pages/images/ model_image/g-arima.png')
    st.image(image)
    image = Image.open('pages/images/ model_image/g-arima-result.png')
    st.image(image)
    st.markdown("")
    
    st.markdown("### π SARIMA X Model")
    
    st.markdown("##### π PPI CPI μ μΈνκ³  νμ΅")
    image = Image.open('pages/images/ model_image/g-sarimax-woppicpi.png')
    st.image(image)
    image = Image.open('pages/images/ model_image/g-arima-result.png')
    st.image(image)
    st.markdown("")
    
    st.markdown("##### π PPI CPIλ‘λ§ νμ΅")
    image = Image.open('pages/images/ model_image/g-sarimax-wppicpi.png')
    st.image(image)
    image = Image.open('pages/images/ model_image/g-sarimax-wppicpi-result.png')
    st.image(image)
    st.markdown("")
    
    st.markdown("##### π λͺ¨λ  Featureλ‘ νμ΅")
    image = Image.open('pages/images/ model_image/g-sarimax-wallfeatures.png')
    st.image(image)
    image = Image.open('pages/images/ model_image/g-sarimax-wallfeatures-result.png')
    st.image(image)
    st.markdown("")
 
    st.markdown("### π Prophet Model")
    image = Image.open('pages/images/ model_image/g-prophet-m.png')
    st.image(image)



elif choice == product[1]:
    st.markdown("## π₯ κ°μ")
    st.markdown("")
    st.markdown("### π ARIMA Model")
    image = Image.open('pages/images/ model_image/pp-arima.png')
    st.image(image)
    image = Image.open('pages/images/ model_image/pp-arima-result.png')
    st.image(image)
    st.markdown("")
    
    st.markdown("### π SARIMA X Model")
    
    st.markdown("##### π PPI CPI μ μΈνκ³  νμ΅")
    image = Image.open('pages/images/ model_image/pp-sarimax-woppicpi.png')
    st.image(image)
    image = Image.open('pages/images/ model_image/pp-sarimax-wocpippi-result.png')
    st.image(image)
    st.markdown("")
    
    st.markdown("##### π PPI CPIλ‘λ§ νμ΅")
    image = Image.open('pages/images/ model_image/pp-sarimax-wcpippi.png')
    st.image(image)
    image = Image.open('pages/images/ model_image/pp-sarimax-wcpippi-result.png')
    st.image(image)
    st.markdown("")
    
    st.markdown("##### π λͺ¨λ  Featureλ‘ νμ΅")
    image = Image.open('pages/images/ model_image/pp-sarimax-wallfeatures.png')
    st.image(image)
    image = Image.open('pages/images/ model_image/pp-sarimax-wallfeatures-result.png')
    st.image(image)
    st.markdown("")
 
    st.markdown("##### π Prophet Model")
    image = Image.open('pages/images/ model_image/p-prophet-m.png')
    st.image(image)


elif choice == product[2]:
    st.markdown("## π  κ³ κ΅¬λ§")
    st.markdown("")
    st.markdown("### π ARIMA Model")
    image = Image.open('pages/images/ model_image/sp-ari.png')
    st.image(image)
    image = Image.open('pages/images/ model_image/sp-ari-result.png')
    st.image(image)
    st.markdown("")
    st.markdown("### π SARIMA Model")
    image = Image.open('pages/images/ model_image/sp-sarima.png')
    st.image(image)
    image = Image.open('pages/images/ model_image/sp-sarima-result.png')
    st.image(image)
    st.markdown("")
    
    st.markdown("### π SARIMA X Model")
    
    st.markdown("##### π PPI CPI μ μΈνκ³  νμ΅")
    image = Image.open('pages/images/ model_image/sp-sarimax-wocpippi.png')
    st.image(image)
    image = Image.open('pages/images/ model_image/sp-sarimax-wocpippi-result.png')
    st.image(image)
    st.markdown("")
    
    st.markdown("##### π PPI CPIλ‘λ§ νμ΅")
    image = Image.open('pages/images/ model_image/sp-sarimax-wcpippi.png')
    st.image(image)
    image = Image.open('pages/images/ model_image/sp-sarimax-wcpippi-result.png')
    st.image(image)
    st.markdown("")
    
    st.markdown("##### π λͺ¨λ  Featureλ‘ νμ΅")
    image = Image.open('pages/images/ model_image/sp-sarimax-wallfeatures.png')
    st.image(image)
    image = Image.open('pages/images/ model_image/sp-sarimax-wallfeatures-result.png')
    st.image(image)
    st.markdown("")
 
    st.markdown("### π Prophet Model")
    image = Image.open('pages/images/ model_image/s-prophet-m.png')
    st.image(image)



elif choice == product[3]:
    st.markdown("## π κΉ»μ")
    st.markdown("")
    st.markdown("### π ARIMA Model")
    image = Image.open('pages/images/ model_image/k-arima.png')
    st.image(image)
    image = Image.open('pages/images/ model_image/k-arima-result.png')
    st.image(image)
    st.markdown("")
    
    st.markdown("### π SARIMA X Model")
    
    st.markdown("##### π PPI CPI μ μΈνκ³  νμ΅")
    image = Image.open('pages/images/ model_image/k-sarimax-wocpippi.png')
    st.image(image)
    image = Image.open('pages/images/ model_image/k-sarimax-wocpippi-result.png')
    st.image(image)
    st.markdown("")
    
    st.markdown("##### π CPIλ‘λ§ νμ΅ (PPIκ°μ΄ μ‘΄μ¬νμ§ μμ)")
    image = Image.open('pages/images/ model_image/k-sarimax-wcpi.png')
    st.image(image)
    image = Image.open('pages/images/ model_image/k-sarimax-wcpi-result.png')
    st.image(image)
    st.markdown("")
    
    st.markdown("##### π λͺ¨λ  Featureλ‘ νμ΅")
    image = Image.open('pages/images/ model_image/k-sarimax-wallfeatures.png')
    st.image(image)
    image = Image.open('pages/images/ model_image/k-sarimax-wallfeatures-result.png')
    st.image(image)
    st.markdown("")
 
    st.markdown("### π Prophet Model")
    image = Image.open('pages/images/ model_image/l-prophet-m.png')
    st.image(image)