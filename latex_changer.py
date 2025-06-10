import streamlit as st

st.title("Latex 시각화 페이지")

user_input = ""
user_input = st.text_input("latex문을 입력하세요")
cleaned = ''.join(user_input.split())

if user_input:
    st.latex(f'{cleaned}')