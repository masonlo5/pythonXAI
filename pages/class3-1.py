import streamlit as st

# 標題：示範如何使用 columns 佈局
st.title("columns")

# 建立 2 欄位，預設等寬
# st.columns(2) 會回傳兩個 column 物件，分別指定給 col1, col2
col1, col2 = st.columns(2)  # 2 columns
col1.button("button1", key="btn1")  # 在 col1 放一個按鈕
col2.button("button2", key="btn2")  # 在 col2 放另一個按鈕

# 指定欄位寬度比 (1:2)，第一欄較窄，第二欄較寬
col1, col2 = st.columns([1, 2])  # 1:2 ratio
col1.button("button3", key="btn3")
col2.button("button4", key="btn4")

# 建立 3 欄
col1, col2, col3 = st.columns(3)  # 3 columns
col1.button("button5", key="btn5")
col2.button("button6", key="btn6")
col3.button("button7", key="btn7")
st.write("---")  # 分隔線

# 使用 with 把元件放進指定的 column 區塊
# 注意原本有個多餘空格錯誤 st. columns -> 已修正為 st.columns
col1, col2 = st.columns([1, 2])
with col1:  # 在 col1 內建立元件
    st.write("col1")  # 在 col1 顯示一些文字
    if st.button("button8", key="btn8"):
        st.balloons()  # 按下按鈕時顯示氣球動畫
with col2:
    st.write("this is col2")
    st.button("button9", key="btn9")

# 動態產生多個欄位：使用者可輸入欄位數量
n = st.number_input("write columns number inside", min_value=1, value=4, step=1)
cols = st.columns(n)  # 產生 n 個 columns，回傳一個 list
for i in range(len(cols)):
    # 透過索引將元件加入對應的欄位
    with cols[i]:
        st.button(f"button{i+1}", key=f"btn{i+10}")

st.write("---")
st.write("columns in a loop")

# 示範在固定兩欄中的多個元件
col1, col2 = st.columns(2)
with col1:
    st.button("button1", key="b")
    st.button("button2", key="b1")
    st.button("button3", key="b2")
with col2:
    # 連續三行文字，顯示在右側欄位
    st.write("this is col2")
    st.write("this is col2")
    st.write("this is col2")
st.write("---")

# 在迴圈中每次建立兩欄，並在每個欄位放不同內容
for i in range(3):
    col1, col2 = st.columns(2)
    with col1:
        # 在第一欄顯示動態文字
        st.write(f"button{i+1}")
    with col2:
        st.write(f"col2_{i+1}")

st.write("---")
st.title("session_state")  # 新段落標題：示範 session_state 的使用

# 簡單變數示範：按鈕改變區域變數（不會持久於 rerun）
ans = 1
if st.button("add 1", key="btn_ans"):
    ans = ans + 1  # 區域變數增加 1
st.write(f"ans={ans}")

# 使用 session_state 儲存狀態，可以跨 rerun 保持變數
if "ans" not in st.session_state:
    st.session_state.ans = 1  # 初始化 session_state

if st.button("add 1", key="btn_ans2"):
    st.session_state.ans = st.session_state.ans + 1  # 更新 session_state
st.write(f"ans={st.session_state.ans}")

# 重置按鈕會觸發 rerun，回到初始狀態（視程式邏輯而定）
if st.button("reset", key="banana"):
    st.rerun()
