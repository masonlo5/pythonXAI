import streamlit as st

st.set_page_config(page_title="My App", layout="wide")
all_pages = {
    "": [
        st.Page("pages/home.py", title ="home", icon="🏠"),
        st.Page("pages/handbook.py", title="notes", icon="📚"),
    ],
    "practice": [
        st.Page("pages/class1-2.py", title="Markdown", icon="📝"),
        st.Page("pages/class2-2.py", title="score", icon="🏆"),
        st.Page("pages/class2-4.py", title="pyramid", icon="🔺"),
        st.Page("pages/class3-1.py", title="columns and session_state", icon="📊"),
        st.Page("pages/class3-2.py", title="food service machine", icon="🍔"),
        st.Page("pages/class3-5.py", title="guess number", icon="❓"),
        st.Page("pages/class4-2.py", title="image display", icon="🖼️"),
        st.Page("pages/class4-3.py", title="product catalog", icon="🛍️"),
        st.Page("pages/class5-2-2.py", title="chat message", icon="💬"),
        st.Page("pages/class5-2-3.py", title="chat history", icon="🗂️"),
        st.Page("pages/class5-2-4.py", title="chat completion", icon="✅")
    ],

}

# use st.navigation
nav = st.navigation(all_pages, position="sidebar")
nav.run()