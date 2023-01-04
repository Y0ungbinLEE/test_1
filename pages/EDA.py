import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
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

# file = 'AgriMarket.csv'

# @st.cache
# def load_data(file):
#     data = pd.read_csv(file)
#     return data

#데이터 로드
url = "https://raw.githubusercontent.com/Y0ungbinLEE/test_1/main/Agri_all.csv"
@st.cache
def load_data(url):
   df = pd.read_csv(url)
   return df

df = load_data(url)


# df = load_data(file)
# df.columns = ["YMD","YM","MD","Product","Price","KRW_USD_EXR","Annual_Call_Rate","item_PPI","item_CPI","Food_Price_Index","Cereals_Price_Index","DayAvg_Temperature","DayDiff_Temperature","DayAvg_RelativeHumidity","DaySum_Rainfall","DayAvg_WindSpeed","DaySum_Sunshine","Warning_Count"]
st.dataframe(df)

st.header(" 🌾 Agricultural Products Price Prediction")

st.markdown("""       """)
# st.dataframe(df)

st.markdown("## ✔ 품목별 EDA")
st.markdown("")
tab1, tab2, tab3, tab4 = st.tabs(["🧄 마늘","🥔 감자", "🍠고구마", "🍃 깻잎" ])

with tab1:
    df_g = df[df["Product"] == "마늘"]
    df_g["M"] = df_g['MD'].map(lambda x:int(str(x)[:-2]))
    df_g["Y"] = df_g['YMD'].map(lambda x:str(x)[:4])
    data_1 = pd.DataFrame(df_g.groupby('Y')['Price'].sum())
    data_1m = pd.DataFrame(df_g.groupby('M')['Price'].sum())
    
    st.dataframe(data_1m) 
          
    plt.figure(figsize=(20, 7))
    st.markdown("")
    st.subheader("💡 파종 및 수확시기")
    st.markdown("- 9 ~ 10월 파종, 5 ~ 6월 수확")
    st.markdown("#### 계절별 가격 추세")
    gh2 = px.line(data_1m)
    st.plotly_chart(gh2)
    st.markdown("#### 연도별 가격 추세")
    gh1 = px.line(data_1)
    st.plotly_chart(gh1)
    st.markdown("#### 기후에 따른 농산물 가격")
    st.markdown("")
    image = Image.open('pages/images/g-weather.png')
    st.image(image)
    st.markdown("")
    st.markdown("#### 이동평균선")
    st.markdown("")
    image = Image.open('pages/images/g-5.png')
    st.image(image)
    st.markdown("")
    st.markdown("##### 마늘 재배는 기온에 많은 영향을 받는다")
    code = '''
    긴 장마와 강한 태풍, 혹한이 이어진 지난해 기후 여파가 가격 상승의 1차 요인으로 꼽힌다. 여기에 코로나19로 인한 산지의 인력 수급 불균형이 가격 상승을 부추기는 구조적 요인으로 지목된다. 
단기간 내 해결되기 힘든 인력 수급 불균형이 농산물 가격을 지속적으로 밀어올릴 전망이다. 한 대형마트의 채소 담당 바이어는 “현지에서는 일할 사람이 없어 원하는 시점에 수확하는 것조차 힘든 상황”이라며 “인건비를 올려주거나 국내 인력을 써야 하기 때문에 이 비용이 소비자 구매가에 지속적으로 반영될 것”이라고 설명
               '''
    st.code(code, language= 'text')
    st.markdown("")

    st.markdown("##### 재배 면적의 감소로 인해 마늘 가격이 상승했다")
    image = Image.open('pages/images/g-harvest.png')
    st.image(image)
    
    
    st.markdown("""""")

with tab2:
    df_p = df[df["Product"] == "감자"]
    df_p["M"] = df_p['MD'].map(lambda x:str(x)[:-2])
    df_p["Y"] = df_p['YMD'].map(lambda x:str(x)[:4])
    data_1 = pd.DataFrame(df_p.groupby('Y')['Price'].sum())
    data_1m = pd.DataFrame(df_p.groupby('M')['Price'].sum())

    st.markdown("💡 파종 및 수확시기")
    st.markdown("- 봄감자:  2 ~ 4월 파종, 6 ~ 7월 수확")
    st.markdown("- 가을감자: 8월 파종,  11월 수확")
    # st.markdown("** 지역별로 90 ~ 100 일 정도재배 후 수확 ** ")
    gh1 = px.line(data_1, title = "가격 추세선")
    st.plotly_chart(gh1)
    gh2 = px.line(data_1m, title = "계절별 가격")
    st.plotly_chart(gh2)

with tab3:
    df_sp = df[df["Product"] == "고구마"]
    df_sp["M"] = df_sp['MD'].map(lambda x:str(x)[:-2])
    df_sp["Y"] = df_sp['YMD'].map(lambda x:str(x)[:4])
    data_1 = pd.DataFrame(df_sp.groupby('Y')['Price'].sum())
    data_1m = pd.DataFrame(df_sp.groupby('M')['Price'].sum())

    st.markdown("💡 파종 및 수확시기")
    st.markdown("- 5 ~ 6월 파종, 10월 수확")
    plt.figure(figsize=(20, 7))
    sns.lineplot(data=df_sp, x="M", y=df_sp["Price"])
    st.markdown("- 가을~겨울 온도가 낮아질수록 수요증가 (군고구마) + 여름 이상기온 많을수록 공급감소 ")
    gh1 = px.line(data_1, title = "가격 추세선")
    st.plotly_chart(gh1)
    gh2 = px.line(data_1m, title = "계절별 가격")
    st.plotly_chart(gh2)

with tab4:
    df_k = df[df["Product"] == "깻잎"]
    df_k["M"] = df_k['MD'].map(lambda x:str(x)[:-2])
    df_k["Y"] = df_k['YMD'].map(lambda x:str(x)[:4])
    data_1 = pd.DataFrame(df_k.groupby('Y')['Price'].sum())
    data_1m = pd.DataFrame(df_k.groupby('M')['Price'].sum())
  
    st.markdown("💡 파종 및 수확시기")
    st.markdown("- 4 ~ 5월 파종, 10월까지 수시로 수확")
    gh1 = px.line(data_1, title = "가격 추세선")
    st.plotly_chart(gh1)
    gh2 = px.line(data_1m, title = "계절별 가격")
    st.plotly_chart(gh2)


st.markdown("")
st.markdown("---")
st.markdown("")

