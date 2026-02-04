import streamlit as st

st.title("🛒 購物籃系統")

# 初始化購物籃
if "cart" not in st.session_state:
    st.session_state.cart = []

# 右上角新增商品區塊
left, right = st.columns([3, 2])
with left:
    st.header("新增商品")
    new_item = st.text_input("請輸入商品名稱：")
with right:
    if st.button("加入商品"):
        if new_item.strip():
            st.session_state.cart.append(new_item.strip())
            st.success(f"已加入：{new_item}")
        else:
            st.warning("商品名稱不能為空白！")

st.header("購物籃內容")

if not st.session_state.cart:
    st.info("購物籃目前是空的。")
else:
    for i, item in enumerate(st.session_state.cart):
        col1, col2 = st.columns([4, 1])
        col1.write(item)
        if col2.button("刪除", key=f"delete_{i}"):
            st.session_state.cart.pop(i)
            st.rerun()
