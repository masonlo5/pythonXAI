import streamlit as st  # 匯入 Streamlit 函式庫，用來建立簡易的網頁介面

# --------- 數字輸入示範 (number_input) ---------
# st.number_input() 可以讓使用者在網頁上輸入數值
# 參數說明：
# - 第一個引數是顯示的提示文字 (label)
# - min_value 是允許輸入的最小值，max_value 是允許輸入的最大值
# - step=1 表示每次增減都是 1（通常用於整數輸入）
# 這裡示範輸入一個介於 0 到 100 的數字
number = st.number_input("請輸入一個數字", min_value=0, max_value=100, step=1)
# st.write() 可以在網頁上顯示文字或變數的值，支援簡單的 Markdown
st.write(f"你輸入的數字是：{number}")  # 顯示使用者剛剛輸入的數字

# 插入一條水平線分隔區塊（外觀用）
st.write("---")

# --------- 成績分級範例 ---------
# 另一個數字輸入範例，這裡用來輸入成績（0-100）
score = st.number_input("請輸入分數", min_value=0, max_value=100, step=1, key="score")
st.write(f"你輸入的分數是：{score}")  # 顯示分數

# 使用 if / elif / else 判斷式來對成績分級
# 條件說明：
# - 如果成績 >= 90，顯示 A
# - 如果成績介於 80 到 89，顯示 B
# - 如果成績介於 70 到 79，顯示 C
# - 如果成績介於 60 到 69，顯示 D
# - 否則顯示 E
if score >= 90:
    st.write("A")  # Top 等級
elif score >= 80 and score <= 89:
    st.write("B")
elif score >= 70 and score <= 79:
    st.write("C")
elif score >= 60 and score <= 69:
    st.write("D")
else:
    st.write("E")

st.write("---")

# --------- 按鈕互動練習 (button) ---------
st.write("### button practice")

# st.button() 會回傳布林值，按下時為 True，否則為 False
# key 參數用來在 Streamlit 狀態中區分不同按鈕
st.button("click me", key="button1")  # 簡單按鈕，沒有綁定動作

# 當按下按鈕時可以執行某些視覺效果或動作
if st.button("click me", key="balloons"):
    # st.balloons() 會在畫面上顯示慶祝用的氣球動畫
    st.balloons()
if st.button("click me", key="snow"):
    # st.snow() 會在畫面上顯示下雪效果（視 Streamlit 版本而定）
    st.snow()

# 再插入一條分隔線作為結尾
st.write("---")