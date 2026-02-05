import streamlit as st
import os

st.title("圖片元件")

st.image("image/酪梨.png", width=300, caption="酪梨")
st.image("image\奇點.png", width=300, caption="奇點")
st.image("image\enric102.png", width=300, caption="enric102")

image_folder = "image"
image_files = os.listdir(image_folder)
image_files.sort()
st.write(image_files)

for image_file in image_files:
    image_path = image_folder + "/" + image_file
    st.image(image_path, width=300)


for image_file in image_files:
    image_path = image_folder + "/" + image_file
    st.image(image_path, use_container_width=True)

st.title("下拉是選單元件")

selected_image = st.selectbox("請選擇圖片", image_files)
st.write("你選擇的圖片是:", selected_image[:-4])
image_path = image_folder + "/" + selected_image
st.image(image_path, width=500)
import time

st.title("網路訊息文件")

cols = st.columns(4)

# success
if cols[0].button("success按鈕"):
    st.success("這是.st.success訊息")
    time.sleep(1)
    st.rerun()
# error
if cols[1].button("error按鈕"):
    st.error("這是st.error訊息")
    time.sleep(1)
    st.rerun()
# warning
if cols[2].button("warning按鈕"):
    st.warning("這是st.warning訊息")
    time.sleep(1)
    st.rerun()
# info
if cols[3].button("info按鈕"):
    st.info("這是st.info訊息")
    time.sleep(1)
    st.rerun()
