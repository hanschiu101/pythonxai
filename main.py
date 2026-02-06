# streamlit run main.py

import streamlit as st


all_pages = {
    "": [
        st.Page("pages/hand_book.py", title="課程筆記", icon="📖"),
    ],
    "📚 程式練習": [
        st.Page("pages/class1-2.py", title="Markdown語法", icon="📝"),
        st.Page("pages/class2-1.py", title="成績等第判斷", icon="📊"),
        st.Page("pages/class2-3.py", title="金字塔系列", icon="🔺"),
        st.Page("pages/class2-7.py", title="排版練習", icon="🔺"),
        st.Page("pages/class3-1.py", title="購物籃系統", icon="🛒"),
        st.Page("pages/class3-5.py", title="猜數字", icon="🎲"),
        st.Page("pages/class4-1.py", title="圖片元件", icon="🖼️"),
        st.Page("pages/class4-2.py", title="shop", icon="🧺"),
        st.Page("pages/class5-4.py", title="對話輸入", icon="👑"),
        st.Page("pages/class5-5.py", title="對話紀錄", icon="💬"),
        st.Page("pages/class5-6.py", title="對話ai", icon="❤️"),
        st.Page("pages/class5-7.py", title="上傳圖片", icon="🤣"),
        st.Page("pages/class5-8.py", title="AI圖片分析", icon="🤖"),
        st.Page("pages/class5-9.py", title="載入動畫", icon="😒"),
        st.Page("pages/class5-10.py", title="AI圖片生成", icon="👌"),
    ],
}
nav = st.navigation(all_pages, position="sidebar")
nav.run()
