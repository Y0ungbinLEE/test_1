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
    page_icon="πΎ",
    layout="wide",
)

# file = 'AgriMarket.csv'

# @st.cache
# def load_data(file):
#     data = pd.read_csv(file)
#     return data

#λ°μ΄ν° λ‘λ
url = "https://raw.githubusercontent.com/Y0ungbinLEE/test_1/main/Agri_all.csv"
@st.cache
def load_data(url):
   df = pd.read_csv(url)
   return df

df = load_data(url)


# df = load_data(file)
# df.columns = ["YMD","YM","MD","Product","Price","KRW_USD_EXR","Annual_Call_Rate","item_PPI","item_CPI","Food_Price_Index","Cereals_Price_Index","DayAvg_Temperature","DayDiff_Temperature","DayAvg_RelativeHumidity","DaySum_Rainfall","DayAvg_WindSpeed","DaySum_Sunshine","Warning_Count"]


st.header(" πΎ Agricultural Products Price Prediction")

st.markdown("""       """)
# st.dataframe(df)

st.markdown("## β νλͺ©λ³ EDA")
st.markdown("")
tab1, tab2, tab3, tab4 = st.tabs(["π§ λ§λ","π₯ κ°μ", "π κ³ κ΅¬λ§", "π κΉ»μ" ])

with tab1:
    df_g = df[df["Product"] == "λ§λ"]
    df_g["M"] = df_g['MD'].map(lambda x:int(str(x)[:-2]))
    df_g["Y"] = df_g['YMD'].map(lambda x:str(x)[:4])
    data_1 = pd.DataFrame(df_g.groupby('Y')['Price'].sum())
    data_1m = pd.DataFrame(df_g.groupby('M')['Price'].sum())
    
             
    plt.figure(figsize=(20, 7))
    st.markdown("""##### λ π§ μ¬λνλ€ νμμ~π΅""")
    st.markdown("")
    st.markdown("#### π‘ νμ’ λ° μνμκΈ°")
    st.markdown("- 9 ~ 10μ νμ’, 5 ~ 6μ μν")
    st.markdown("")
    st.markdown("#### κ³μ λ³ κ°κ²© μΆμΈ")
    gh2 = px.line(data_1m)
    st.plotly_chart(gh2)
    st.markdown("#### μ°λλ³ κ°κ²© μΆμΈ")
    gh1 = px.line(data_1)
    st.plotly_chart(gh1)
    st.markdown("#### κΈ°νμ λ°λ₯Έ λμ°λ¬Ό κ°κ²©")
    st.markdown("")
    image = Image.open('pages/images/g-weather.png')
    st.image(image)
    st.markdown("")
    st.markdown("#### 5λ κ°κ²© λ³νμΆμ΄")
    st.markdown("")
    image = Image.open('pages/images/g-5.png')
    st.image(image)
    st.markdown("")
    
    st.markdown("")
    st.markdown("")
    st.markdown("""
    ### π SUMMARY
    ##### β λ§λμ κ°κ²© λ³λ μμΈ
    1. μ¬λ°°μκΈ°, μ¬λ°°λ©΄μ κ³Ό κΈ°μ¨μ λ§μ μν₯μ λ°μ (λ§λ μμ‘ μ μ¨μ 18~20β, 25β μ΄μμμλ μμ‘ μ μ§)
    2. μ½λ‘λ19λ‘ μΈν μΈλ ₯ μκΈ λΆκ· ν
    """)
    
    st.markdown("")
    st.markdown("")
    st.markdown("###### **κΈ°μ¨**μ λ§μ μν₯μ λ°λ λ§λ μ¬λ°°")
    st.markdown(""" 
    β‘οΈ κ΄λ ¨κΈ°μ¬: 
    κΈ΄ μ₯λ§μ κ°ν νν, νΉνμ΄ μ΄μ΄μ§ μ§λν΄ **κΈ°ν μ¬νκ° κ°κ²© μμΉμ 1μ°¨ μμΈ**μΌλ‘ κΌ½νλ€. μ¬κΈ°μ **μ½λ‘λ19λ‘ μΈν μ°μ§μ μΈλ ₯ μκΈ λΆκ· νμ΄ κ°κ²© μμΉμ λΆμΆκΈ°λ κ΅¬μ‘°μ  μμΈ**μΌλ‘ μ§λͺ©λλ€. 
    """)
    st.markdown(""" 
    μΆμ²: [https://www.hankyung.com/economy/article/2021051867001](https://www.hankyung.com/economy/article/2021051867001)
    """)                
    st.markdown("")
    st.markdown("")
    st.markdown("###### **μ¬λ°° λ©΄μ **μ κ°μλ‘ μΈν κ°κ²©μμΉ")
    image = Image.open('pages/images/g-harvest.png')
    st.image(image)



with tab2:
    df_p = df[df["Product"] == "κ°μ"]
    df_p["M"] = df_p['MD'].map(lambda x:int(str(x)[:-2]))
    df_p["Y"] = df_p['YMD'].map(lambda x:str(x)[:4])
    data_1 = pd.DataFrame(df_p.groupby('Y')['Price'].sum())
    data_1m = pd.DataFrame(df_p.groupby('M')['Price'].sum())

    st.markdown("""##### π₯ ν©λλ€ β€οΈ""")
    st.markdown("")
    st.markdown("#### π‘ νμ’ λ° μνμκΈ°")
    st.markdown("- λ΄κ°μ:  2 ~ 4μ νμ’, 6 ~ 7μ μν")
    st.markdown("- κ°μκ°μ: 8μ νμ’,  11μ μν")
    st.markdown("")
    st.markdown("#### κ³μ λ³ κ°κ²© μΆμΈ")
    gh2 = px.line(data_1m)
    st.plotly_chart(gh2)
    st.markdown("#### μ°λλ³ κ°κ²© μΆμΈ")
    gh1 = px.line(data_1)
    st.plotly_chart(gh1)
    st.markdown("#### κΈ°νμ λ°λ₯Έ λμ°λ¬Ό κ°κ²©")
    st.markdown("")
    image = Image.open('pages/images/p_weather.png')
    st.image(image)
    st.markdown("- κ°μ κ°κ²©μ μμ°μ¬ν΄λ₯Ό μ μΈνκ³  κΈ°μ¨, κ°μλμ μν₯μ ν¬κ² λ°μ§ μλλ€")
    st.markdown("")
    st.markdown("##### π€ 2018λμ κ°κ²©μ΄ κΈλ±ν μ΄μ ?")
    st.markdown(""" 
    1. 2017λ κ°μ μ¬λ°°λ©΄μ  κ°μλ‘ μΈν΄ μμ°λλ κ°μν¨μ λ°λΌ μ μ₯ λ¬Όλ λΆμ‘± (μμ > κ³΅κΈ)
    2. ννλ‘ μΈν μΆν μ§μ°
    β‘οΈ κ΄λ ¨κΈ°μ¬: 
    λ΄ κ°μλ μ΄λ‘μ μΈ ν­λ±μ λ§μλ€. μ§λν΄ κ°μκ°μ μμ°μ΄ κ°μνκ³  μ μ₯κ°μ λ¬Όλμ΄ λΆμ‘±νλλ°λ€ ννλ‘ μΈν΄ μμ€λ΄κ°μ μΆνλ§μ  μ§μ°λ νμ΄λ€. 
    """)
    st.markdown(""" 
    μΆμ²: [http://www.ikpnews.net/news/articleView.html?idxno=34525](http://www.ikpnews.net/news/articleView.html?idxno=34525)
    """)   
    st.markdown("")
    st.markdown("#### 5λ κ°κ²© λ³νμΆμ΄")
    st.markdown("")
    image = Image.open('pages/images/p-5.png')
    st.image(image)

    st.markdown("")
    st.markdown("")
    
    st.markdown("""
    ### π SUMMARY
    ##### βΒ κ°μ κ°κ²© λ³λ μμΈ
    1. μ¬λ°°μκΈ°μ μμ°μ¬ν΄ (νν, νν) λ§μ μν₯μ λ°μ
    2. 2018λμ νν λ° ννλ‘ μΈν κ°κ²© μμΉ 
    """)

    st.markdown(""" 
    β‘οΈ κ΄λ ¨κΈ°μ¬: 
    2018λμλ μλ³λ‘ 'μ΄μκΈ°ν'κ° κ³μλλ€λ λΆμ κ²°κ³Όκ° λμλ€.Β μ°μ΄ κ²¨μΈμλ λ§ΉμΆμκ° μ°Ύμμ€κ³  μ¬λ¦μλ νν 2κ°κ° μλ₯νμΌλ©°, μ₯λ§λ μ§§μλ λ°λ©΄ λ¬΄λμλ κΈΈκ³  μ¬νλ€.
    """)
    st.markdown("""     
    μΆμ² : [http://www.greenpostkorea.co.kr/news/articleView.html?idxno=100176](http://www.greenpostkorea.co.kr/news/articleView.html?idxno=100176)
    """)  
    

with tab3:
    df_sp = df[df["Product"] == "κ³ κ΅¬λ§"]
    df_sp["M"] = df_sp['MD'].map(lambda x:int(str(x)[:-2]))
    df_sp["Y"] = df_sp['YMD'].map(lambda x:str(x)[:4])
    data_1 = pd.DataFrame(df_sp.groupby('Y')['Price'].sum())
    data_1m = pd.DataFrame(df_sp.groupby('M')['Price'].sum())

    st.markdown(""" ##### κ²¨μΈμλ μ­μ π κ΅¬λ§ """)
    st.markdown("")
    st.markdown("#### π‘ νμ’ λ° μνμκΈ°")
    st.markdown("- 5 ~ 6μ νμ’, 10μ μν")
    st.markdown("#### κ³μ λ³ κ°κ²© μΆμΈ")
    gh2 = px.line(data_1m)
    st.plotly_chart(gh2)
    st.markdown("#### μ°λλ³ κ°κ²© μΆμΈ")
    gh1 = px.line(data_1)
    st.plotly_chart(gh1)
    st.markdown("#### κΈ°νμ λ°λ₯Έ λμ°λ¬Ό κ°κ²©")
    st.markdown("")
    image = Image.open('pages/images/sp-weather.png')
    st.image(image)
    st.markdown("##### κ³ κ΅¬λ§ κ°κ²©μ μμ°μ¬ν΄ (νν, νν), κΈ°μ¨κ³Ό κ°μλ λ±μ μν₯μ λ°λ κ²μΌλ‘ λ³΄μΈλ€.")
    st.markdown("- κ°μ~κ²¨μΈ μ¨λκ° λ?μμ§μλ‘ μμμ¦κ° (κ΅°κ³ κ΅¬λ§) + μ¬λ¦ μ΄μκΈ°μ¨ λ§μμλ‘ κ³΅κΈκ°μ")
    
    st.markdown("")
    st.markdown("#### 5λ κ°κ²© λ³νμΆμ΄")
    st.markdown("")
    image = Image.open('pages/images/sp-5.png')
    st.image(image)
    st.markdown("")
    st.markdown("""
    ### π SUMMARY  
    ##### βΒ κ³ κ΅¬λ§ κ°κ²© λ³λ μμΈ
    1. κ²¨μΈμ²  κ°μ μμ μ¦κ°
    2. ννκ³Ό μ₯λ§λ‘ μΈν μμ°λ κ°μ
    β‘οΈ κ΄λ ¨κΈ°μ¬:
    κ΅°κ³ κ΅¬λ§ λ± κ³ κ΅¬λ§ κ°μ μμ μ¦κ°λ λ¬Όλ‘  μ¬μ¬λ¦ μ¦μ ννκ³Ό κΈ΄ μ₯λ§λ‘ μ°μ§ μνμ μ΄λ €μμ κ²ͺμΌλ©΄μ κ³ κ΅¬λ§ μμ° λ¬Όλμ΄ μ€μ΄λ  νμ΄λ€.
    """)
    
    st.markdown("""  
    μΆμ²: [https://m.edaily.co.kr/news/Read?newsId=02686326625962768&mediaCodeNo=257&utm_source=https://www.google.com/](https://m.edaily.co.kr/news/Read?newsId=02686326625962768&mediaCodeNo=257&utm_source=https://www.google.com/)
    """)


with tab4:
    df_k = df[df["Product"] == "κΉ»μ"]
    df_k["M"] = df_k['MD'].map(lambda x:int(str(x)[:-2]))
    df_k["Y"] = df_k['YMD'].map(lambda x:str(x)[:4])
    data_1 = pd.DataFrame(df_k.groupby('Y')['Price'].sum())
    data_1m = pd.DataFrame(df_k.groupby('M')['Price'].sum())
  
    st.markdown(""" ##### π λΌμ£ΌκΈ° κ°λ₯? λΆκ°λ₯? """)
    st.markdown("")
    st.markdown("#### π‘ νμ’ λ° μνμκΈ°")
    st.markdown(" 4 ~ 5μμ νμ’, 10μκΉμ§ νμν  λλ§λ€ μν")
    st.markdown("#### κ³μ λ³ κ°κ²© μΆμΈ")
    gh2 = px.line(data_1m)
    st.plotly_chart(gh2)
    st.markdown("#### μ°λλ³ κ°κ²© μΆμΈ")
    gh1 = px.line(data_1)
    st.plotly_chart(gh1)
    st.markdown("#### κΈ°νμ λ°λ₯Έ λμ°λ¬Ό κ°κ²©")
    st.markdown("")
    
    st.markdown("")                
    st.markdown("#### Warning Count")
    image = Image.open('pages/images/k-warning.png')
    st.image(image)
    st.markdown("- ν΄κ° μ§λ μλ‘ Warning countκ° λ°μνλ λΉλκ° μ¦κ°νλ€. e.g. νλμ£Όμλ³΄, ν­μ°μ£Όμλ³΄ λ±")
    st.markdown("")
    st.markdown("#### μΌλ³ νκ·  μλμ΅λ")
    image = Image.open('pages/images/k-humid.png')
    st.image(image)
    st.markdown("")
    st.markdown("#### μΌλ³ νκ·  νμ")
    image = Image.open('pages/images/k-windspeed.png')
    st.image(image)
    st.markdown("- λ°λμ μν₯μ λ°μ")
    st.markdown("")
    st.markdown("#### 5λ κ°κ²© λ³νμΆμ΄")
    st.markdown("")
    image = Image.open('pages/images/k-5.png')
    st.image(image)
    st.markdown("")
    st.markdown("")
    st.markdown('''
    ### π SUMMARY  
    ##### βΒ κΉ»μ κ°κ²© λ³λ μμΈ
    1. μμΆλ μ¬λ°°κΈ°κ°μ΄ μ§§μ μκΈμ΄ λ€λ₯Έ λμ°λ¬Όλ€μ λΉνμ¬ μνν μ΄λ£¨μ΄μ§λ νΈμ΄μ§λ§ κΈ°νκ° μκΈμ ν° μν₯μ λΌμΉλ€κ³  λ³Ό μ μλ€. κ·Έλ‘ μΈνμ¬ κ°κ²© λ³λμ΄ ν­μ΄ λ§€μ° μ§§μ νΈμ΄λ€.
    2. λ€λ₯Έ κΈ°νλ€λ³΄λ€ μΌμ‘°λμ κ°μ₯ λ§μ μν₯μ λ°λ μμ±μμ΄κΈ°μ κ΅¬λ¦μ΄ λ§μ΄ λΌλ λ , ν­μ°μ μν₯μ κ°μ₯ λ§μ΄ λ°λλ€.
    3. μΌμ‘°λμ κ°μ₯ λ§μ μν₯μ λ°λλ€κ³ λ νλ μλΆμ μ μ§ν  μ μμ μ λμ ν­μΌμλ μ·¨μ½ν λͺ¨μ΅μ λ³΄μΈλ€.
    
    β‘οΈ κ΄λ ¨κΈ°μ¬:
    ν­μΌμΌλ‘ μΈν΄ μΌκ²Ήμ΄ κ°κ²©κ³Ό λ§λ¨Ήλ μμΆμ κΉ»μ
    ''')
    st.markdown("""  
    μΆμ²: [https://www.hankyung.com/economy/article/201908094787Y)
    """)
    st.markdown("""  
    κΈ΄ μ₯λ§μ νλ¦°λ λ‘ μκΈμ΄ λΆμν΄μ§λ μμ±μ
    """)
    st.markdown(''' 
    μΆμ²: [https://www.yna.co.kr/view/AKR20200810076100530)
    ''')
st.markdown("")
st.markdown("---")


