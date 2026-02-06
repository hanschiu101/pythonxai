import streamlit as st

uploaded_file = st.file_uploader("上傳圖片", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="上傳的圖片", width=300)
