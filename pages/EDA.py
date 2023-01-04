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
    
             
    plt.figure(figsize=(20, 7))
    st.markdown("""##### 나 🧄 사랑한다 했잖아~🎵""")
    st.markdown("")
    st.markdown("#### 💡 파종 및 수확시기")
    st.markdown("- 9 ~ 10월 파종, 5 ~ 6월 수확")
    st.markdown("")
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
    st.markdown("#### 5년 가격 변화추이")
    st.markdown("")
    image = Image.open('pages/images/g-5.png')
    st.image(image)
    st.markdown("")
    
    st.markdown("")
    st.markdown("")
    st.markdown("""
    ### 📌 SUMMARY
    ##### ✅ 마늘의 가격 변동 요인
    1. 재배시기, 재배면적과 기온에 많은 영향을 받음 (마늘 생육 적온은 18~20℃, 25℃ 이상에서는 생육 정지)
    2. 코로나19로 인한 인력 수급 불균형
    """)
    
    st.markdown("")
    st.markdown("")
    st.markdown("###### **기온**에 많은 영향을 받는 마늘 재배")
    st.markdown(""" 
    ➡️ 관련기사: 
    긴 장마와 강한 태풍, 혹한이 이어진 지난해 **기후 여파가 가격 상승의 1차 요인**으로 꼽힌다. 여기에 **코로나19로 인한 산지의 인력 수급 불균형이 가격 상승을 부추기는 구조적 요인**으로 지목된다. 
    """)
    st.markdown(""" 
    출처: [https://www.hankyung.com/economy/article/2021051867001](https://www.hankyung.com/economy/article/2021051867001)
    """)                
    st.markdown("")
    st.markdown("")
    st.markdown("###### **재배 면적**의 감소로 인한 가격상승")
    image = Image.open('pages/images/g-harvest.png')
    st.image(image)



with tab2:
    df_p = df[df["Product"] == "감자"]
    df_p["M"] = df_p['MD'].map(lambda x:int(str(x)[:-2]))
    df_p["Y"] = df_p['YMD'].map(lambda x:str(x)[:4])
    data_1 = pd.DataFrame(df_p.groupby('Y')['Price'].sum())
    data_1m = pd.DataFrame(df_p.groupby('M')['Price'].sum())

    st.markdown("""##### 🥔 합니다 ❤️""")
    st.markdown("")
    st.markdown("#### 💡 파종 및 수확시기")
    st.markdown("- 봄감자:  2 ~ 4월 파종, 6 ~ 7월 수확")
    st.markdown("- 가을감자: 8월 파종,  11월 수확")
    st.markdown("")
    st.markdown("#### 계절별 가격 추세")
    gh2 = px.line(data_1m)
    st.plotly_chart(gh2)
    st.markdown("#### 연도별 가격 추세")
    gh1 = px.line(data_1)
    st.plotly_chart(gh1)
    st.markdown("#### 기후에 따른 농산물 가격")
    st.markdown("")
    image = Image.open('pages/images/p_weather.png')
    st.image(image)
    st.markdown("- 감자 가격은 자연재해를 제외하고 기온, 강수량에 영향을 크게 받지 않는다")
    st.markdown("")
    st.markdown("##### 🤔 2018년에 가격이 급등한 이유?")
    st.markdown(""" 
    1. 2017년 감자 재배면적 감소로 인해 생산량도 감소함에 따라 저장 물량 부족 (수요 > 공급)
    2. 한파로 인한 출하 지연
    ➡️ 관련기사: 
    봄 감자는 이례적인 폭등을 맞았다. 지난해 가을감자 생산이 감소하고 저장감자 물량이 부족했던데다 한파로 인해 시설봄감자 출하마저 지연된 탓이다. 
    """)
    st.markdown(""" 
    출처: [http://www.ikpnews.net/news/articleView.html?idxno=34525](http://www.ikpnews.net/news/articleView.html?idxno=34525)
    """)   
    st.markdown("")
    st.markdown("#### 5년 가격 변화추이")
    st.markdown("")
    image = Image.open('pages/images/p-5.png')
    st.image(image)

    st.markdown("")
    st.markdown("")
    
    st.markdown("""
    ### 📌 SUMMARY
    ##### ✅ 감자 가격 변동 요인
    1. 재배시기와 자연재해 (태풍, 한파) 많은 영향을 받음
    2. 2018년에 태풍 및 한파로 인한 가격 상승 
    """)

    st.markdown(""" 
    ➡️ 관련기사: 
    2018년에는 월별로 '이상기후'가 계속됐다는 분석 결과가 나왔다. 연초 겨울에는 맹추위가 찾아오고 여름에는 태풍 2개가 상륙했으며, 장마는 짧았던 반면 무더위는 길고 심했다.
    """)
    st.markdown("""     
    출처 : [http://www.greenpostkorea.co.kr/news/articleView.html?idxno=100176](http://www.greenpostkorea.co.kr/news/articleView.html?idxno=100176)
    """)  
    

with tab3:
    df_sp = df[df["Product"] == "고구마"]
    df_sp["M"] = df_sp['MD'].map(lambda x:int(str(x)[:-2]))
    df_sp["Y"] = df_sp['YMD'].map(lambda x:str(x)[:4])
    data_1 = pd.DataFrame(df_sp.groupby('Y')['Price'].sum())
    data_1m = pd.DataFrame(df_sp.groupby('M')['Price'].sum())

    st.markdown(""" ##### 겨울에는 역시 🍠구마 """)
    st.markdown("")
    st.markdown("#### 💡 파종 및 수확시기")
    st.markdown("- 5 ~ 6월 파종, 10월 수확")
    st.markdown("#### 계절별 가격 추세")
    gh2 = px.line(data_1m)
    st.plotly_chart(gh2)
    st.markdown("#### 연도별 가격 추세")
    gh1 = px.line(data_1)
    st.plotly_chart(gh1)
    st.markdown("#### 기후에 따른 농산물 가격")
    st.markdown("")
    image = Image.open('pages/images/sp-weather.png')
    st.image(image)
    st.markdown("##### 고구마 가격은 자연재해 (태풍, 한파), 기온과 강수량 등에 영향을 받는 것으로 보인다.")
    st.markdown("- 가을~겨울 온도가 낮아질수록 수요증가 (군고구마) + 여름 이상기온 많을수록 공급감소")
    
    st.markdown("")
    st.markdown("#### 5년 가격 변화추이")
    st.markdown("")
    image = Image.open('pages/images/sp-5.png')
    st.image(image)
    st.markdown("")
    st.markdown("""
    ### 📌 SUMMARY  
    ##### ✅ 고구마 가격 변동 요인
    1. 겨울철 간식 수요 증가
    2. 태풍과 장마로 인한 생산량 감소
    ➡️ 관련기사:
    군고구마 등 고구마 간식 수요 증가는 물론 올여름 잦은 태풍과 긴 장마로 산지 수확에 어려움을 겪으면서 고구마 생산 물량이 줄어든 탓이다.
    """)
    
    st.markdown("""  
    출처: [https://m.edaily.co.kr/news/Read?newsId=02686326625962768&mediaCodeNo=257&utm_source=https://www.google.com/](https://m.edaily.co.kr/news/Read?newsId=02686326625962768&mediaCodeNo=257&utm_source=https://www.google.com/)
    """)


with tab4:
    df_k = df[df["Product"] == "깻잎"]
    df_k["M"] = df_k['MD'].map(lambda x:int(str(x)[:-2]))
    df_k["Y"] = df_k['YMD'].map(lambda x:str(x)[:4])
    data_1 = pd.DataFrame(df_k.groupby('Y')['Price'].sum())
    data_1m = pd.DataFrame(df_k.groupby('M')['Price'].sum())
  
    st.markdown(""" ##### 🍃 떼주기 가능? 불가능? """)
    st.markdown("")
    st.markdown("#### 💡 파종 및 수확시기")
    st.markdown(" 4 ~ 5월에 파종, 10월까지 필요할 때마다 수확")
    st.markdown("#### 계절별 가격 추세")
    gh2 = px.line(data_1m)
    st.plotly_chart(gh2)
    st.markdown("#### 연도별 가격 추세")
    gh1 = px.line(data_1)
    st.plotly_chart(gh1)
    st.markdown("#### 기후에 따른 농산물 가격")
    st.markdown("")
    
    st.markdown("")                
    st.markdown("#### Warning Count")
    image = Image.open('pages/images/k-warning.png')
    st.image(image)
    st.markdown("- 해가 지날수록 Warning count가 발생하는 빈도가 증가한다. e.g. 풍랑주의보, 폭우주의보 등")
    st.markdown("")
    st.markdown("#### 일별 평균 상대습도")
    image = Image.open('pages/images/k-humid.png')
    st.image(image)
    st.markdown("")
    st.markdown("#### 일별 평균 풍속")
    image = Image.open('pages/images/k-windspeed.png')
    st.image(image)
    st.markdown("- 바람에 영향을 받음")
    st.markdown("")
    st.markdown("#### 5년 가격 변화추이")
    st.markdown("")
    image = Image.open('pages/images/k-5.png')
    st.image(image)
    st.markdown("")
    st.markdown("")
    st.markdown('''
    ### 📌 SUMMARY  
    ##### ✅ 깻잎 가격 변동 요인
    1. 상추는 재배기간이 짧아 수급이 다른 농산물들에 비하여 원활히 이루어지는 편이지만 기후가 수급에 큰 영향을 끼친다고 볼 수 있다. 그로 인하여 가격 변동이 폭이 매우 짧은 편이다.
    2. 다른 기후들보다 일조량에 가장 많은 영향을 받는 잎채소이기에 구름이 많이 끼는 날, 폭우에 영향을 가장 많이 받는다.
    3. 일조량에 가장 많은 영향을 받는다고는 하나 수분을 유지할 수 없을 정도의 폭염에는 취약한 모습을 보인다.
    
    ➡️ 관련기사:
    폭염으로 인해 삼겹살 가격과 맞먹는 상추와 깻잎
    ''')
    st.markdown("""  
    출처: [https://www.hankyung.com/economy/article/201908094787Y)
    """)
    st.markdown("""  
    긴 장마와 흐린날로 수급이 불안해지는 잎채소
    """)
    st.markdown(''' 
    출처: [https://www.yna.co.kr/view/AKR20200810076100530)
    ''')
st.markdown("")
st.markdown("---")


