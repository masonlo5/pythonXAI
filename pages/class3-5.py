import random
import streamlit as st
import time

if "answer" not in st.session_state:
    st.session_state.answer = random.randint(1, 100)  # 程式會從 1 到 100 中隨機選一個數字作為答案
if "max_num" not in st.session_state:
    st.session_state.max_num = 100
if "min_num" not in st.session_state:
    st.session_state.min_num = 1

st.title("猜數字遊戲")


print("歡迎來到猜數字遊戲！我已經選好了一個 1 到 100 之間的數字。")  # 開場提示
print("請開始猜吧！")  # 提示玩家開始輸入

# 主迴圈：反覆要求玩家輸入，直到猜中為止

        # input() 會回傳字串，需要用 int() 轉為整數
        # f-string 用法：f"...{變數}..."，可以把變數插入字串中
guess = st.number_input(f"請輸入{st.session_state.min_num} 到 {st.session_state.max_num}的整數：", step=1)
if st.button("猜"):
        # 比較玩家輸入與答案的關係，並根據結果提示玩家
     if guess < st.session_state.answer:
            st.write("再大一點")  # 提示要猜更大的數
            # 若玩家猜的數字比目前的下界還大，更新下界
            if guess > st.session_state.min_num:
                st.session_state.min_num = guess
     elif guess > st.session_state.answer:
            st.write("再小一點")  # 提示要猜更小的數
            # 若玩家猜的數字比目前的上界還小，更新上界
            if guess < st.session_state.max_num:
                st.session_state.max_num = guess
     else:
         st.write("猜中了！恭喜你！")
         st.balloons()

     time.sleep(1)
     st.rerun()
    

