import streamlit as st

st.chat_message("user").write("這是使用者的訊息")
st.chat_message("assistant").write("這是AI的訊息")


# 範例對話紀錄
history = [
    {"role": "user", "content": "你好,ai"},
    {"role": "assistant", "content": "你好!有什麼我可以幫助你的嗎?"},
    {"role": "user", "content": "請問st.chat_message()怎麼用?"},
    {
        "role": "assistant",
        "content": "st.chat_message()是可以用聊天方塊的顯示訊息!",
    },
]

# 用迴圈顯示聊天方塊
for message in history:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    else:
        st.chat_message("assistant").write(message["content"])
