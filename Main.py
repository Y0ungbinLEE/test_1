import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(
    page_title="Agriculture",
    page_icon="πΎ",
    layout="wide",
)
st.markdown("""**Likelion AI SCHOOL7 Final Project**""")
st.title("π Queen μΉνμλ²³ 7μΈ")
st.markdown("""**Team members**  μ‘μΉν, μ±λμ½, λ°μ±μ©, λ°νμ , μ°μ , μ΄μλΉ""")
st.markdown("---")

st.header(" πΎ Agricultural Products Price Prediction")

st.markdown("""       """)


st.markdown("### π νλ‘μ νΈ μ μ  λ°°κ²½")
st.markdown("""             """)

image = Image.open('pages/images/main.png')
st.image(image)

st.markdown("""    ##### #μλ μλ³΄ #κ³‘λ¬Ό μκΈλ₯  κ°μ #κ²½μ  μΉ¨μ²΄ #μΈκ΅ λΆμ #κΈ°ν λ³ν """)
st.markdown("""μ°ν¬λΌμ΄λ μ μ μ¬νλ‘ μΈκ³ κ³³κ³³μμ μλ μμ°λ λ° κ³΅κΈμ΄ κ°μνκ³  μμμ¬ κ°κ²©μ΄ μΉμκ³  μμ΅λλ€. UNμ μ μμ΄ μΌκΈ°ν μλμκΈ°κ° μμΌλ‘ μλ λμ μ§μλ  μ μλ€κ³  κ²½κ³ νμ΅λλ€.
βμλμκΈ°'κ° νΌλΆλ‘ μλΏμ§ μλ λ¬Έμ μ²λΌ λκ»΄μ§ μλ μλλ°μ. μ°λ¦¬λ μ΄λ―Έ 10λ μ , κΈλ±ν μμμ¬ κ°κ²©μΌλ‘ μΈν΄ μ μ¬ν μΆ©κ²©μ κ²½ννμκ³ , κ°μ₯ μ΅κ·Όμλ μ½λ‘λ19 ν¬λ°λ―Ή μ΄κΈ°μ μλ λΆμ‘±μ κ²ͺκΈ°λ νμ΅λλ€. 
(μΆμ²: κ·Έλ¦°νΌμ€ μμΈμ¬λ¬΄μ,λ°₯μμ μννλ βμλ μκΈ°β... κ·Έ ν΄λ²μ?)""")

st.markdown("###### β‘οΈ λΆμμ ν μ μΈ μ μλ μκΈ μκΈ°μ λλΉλ°©μ λ§λ ¨μ μν λμ°λ¬Ό κ°κ²© μμΈ‘μ μ§ν ")

st.markdown("""            """)
st.markdown("""             """)
st.markdown("### π νλ‘μ νΈ κ³Όμ ")
st.markdown("""             """)
st.markdown("""  
            - ##### [EDA λ° μΈμ¬μ΄νΈ](https://y0ungbinlee-test-1-main-gfhk1e.streamlit.app/EDA)
            - ##### [νλͺ©λ³ λͺ¨λΈλ§](https://y0ungbinlee-test-1-main-gfhk1e.streamlit.app/Modeling_by_Product)
""")

# st.markdown("### π νλ‘μ νΈ κ²°κ³Ό")


# st.sidebar.header('Agricultural Products Price Prediction')
# st.sidebar.markdown("""
#     ### 

#     ### β ννμ΄μ§
#     github : [Git](https://github.com/Sankamita3131/Agricultural-Products-Price-Prediction-)
# """)


st.markdown("")
st.markdown("---")