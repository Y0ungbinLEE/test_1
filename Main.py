import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(
    page_title="Agriculture",
    page_icon="🌾",
    layout="wide",
)
st.markdown("""**Likelion AI SCHOOL7 Final Project**""")
st.title("👑 Queen치현자벳 7세")
st.markdown("""**Team members** 송치현, 성동엽, 박성용, 박혜정, 우신, 이영빈""")
st.markdown("---")

st.header(" 🌾 Agricultural Products Price Prediction")

st.markdown("""       """)


st.markdown("### 📌 프로젝트 선정 배경")
st.markdown("""             """)

image = Image.open('pages/images/main.png')
st.image(image)

st.markdown("""    #### #식량 안보 #곡물 자급률 감소 #경제 침체 #외교 분쟁 #기후 변화 """)
st.markdown("""우크라이나 전쟁 여파로 세계 곳곳에서 식량 생산량 및 공급이 감소하고 식자재 가격이 치솟고 있습니다. UN은 전쟁이 야기한 식량위기가 앞으로 수년 동안 지속될 수 있다고 경고했습니다.
‘식량위기'가 피부로 와닿지 않는 문제처럼 느껴질 수도 있는데요. 우리는 이미 10년 전, 급등한 식자재 가격으로 인해 유사한 충격을 경험했었고, 가장 최근에는 코로나19 팬데믹 초기에 식량 부족을 겪기도 했습니다. 
(출처: 그린피스 서울사무소,밥상을 위협하는 ‘식량 위기’... 그 해법은?)""")

st.markdown("##### ➡️ 불안정한 정세 속 식량 수급 위기에 대비방안 마련을 위한 농산물 가격 예측을 진행 ")

st.markdown("""            """)
st.markdown("""             """)
st.markdown("### 📌 프로젝트 과정")
st.markdown("""             """)
st.markdown("""  
            - ##### EDA 및 품목 선정
            - ##### 예측 모델링
""")

st.markdown("### 📌 프로젝트 결과")


st.sidebar.header('Agricultural Products Price Prediction')
st.sidebar.markdown("""
    ### 

    ### ☘ 홈페이지
    github : [Git](https://github.com/Sankamita3131/Agricultural-Products-Price-Prediction-)
""")


st.markdown("")
st.markdown("---")