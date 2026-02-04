import streamlit as st
import os

st.title("課堂筆記")

folder_path = "markdown"
files = os.listdir(folder_path)
files.sort()
selected_file = []
for file in files:
    if file.endswith(".md"):
        with st.expander(file[:-3]):
            file_path = folder_path + "/" + file
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                st.write(content)
