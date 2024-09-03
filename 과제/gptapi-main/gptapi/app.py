import streamlit as st
import requests
import pandas as pd


# 프론트엔드

st.title("광고 문구를 생성해주는 서비스앱")
product_name = st.text_input("제품명", "")
detail = st.text_input("주요 내용", "")
options = st.multiselect("광고 문구의 느낌", options=["기본", "재밌게", "차분하게", "과장스럽게", "참신하게", "고급스럽게", "센스있게", "아름답게"], default=["기본"])


url = "http://127.0.0.1:8000/create_ad"

if st.button('광고 문구 생성하기'):
    try:
        response = requests.post(url,
        json={
            "product_name": product_name,
            "details": detail,
            "tone_and_manner": ", ".join(options)
        })
        ad = response.json()["ad"]
        st.success(ad)
    except:
        st.error("연결 실패!")


try:
    response = requests.get("http://127.0.0.1:8000/get_ad")
    datas = response.json()
    if datas:
        df = pd.DataFrame(datas)
        st.table(df)
    else:
        st.warning("광고 문구 데이터가 없습니다.")
except:
    st.error("서버 연결에 실패했습니다.")
