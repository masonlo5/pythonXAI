import streamlit as st  # 匯入 Streamlit 函式庫，用來建立簡易的網頁介面

# st.number_input() 可以在網頁上顯示數值輸入欄位，
# 參數說明：
#  - 第一個參數為顯示在畫面上的提示文字
#  - min_value 設定可輸入的最小值
#  - max_value 設定可輸入的最大值
# 回傳值為使用者輸入的數字（型態為 int 或 float，視參數而定）
number = st.number_input("請輸入一個數字", min_value=1, max_value=9)

# 下面使用 for 迴圈從 1 到 number（包含 number）
# range(1, number+1) 會產生 1, 2, ..., number
# 在迴圈中我們使用 st.write() 將結果輸出到網頁上
# f"{i}" * i 表示將數字 i 轉成字串後重複 i 次，
# 例如 i=3 時，f"{i}"*i -> "333"
for i in range(1, number + 1):
   st.write(f"{i}" * i)

 