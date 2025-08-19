# for 迴圈
# for 會搭配 in 來使用，in 後方要放一個「可疊代(iterable)」的物件
# 最常見的搭配是用 range() 來產生數值序列
# range(5) 會產生 0,1,2,3,4（包含起始值 0，不包含結束值 5）
# 下面範例示範 i 作為迴圈變數，會依序取得序列中的每個值
for i in range(5):
    print(i)

# range(起始, 結束) 會產生從 起始 到 (結束-1) 的整數序列
# 例如 range(1, 5) 會產生 1,2,3,4（包含 1，不包含 5）
for i in range(1, 5):
    print(i)

# range(起始, 結束, 步長) 可以指定步長
# 例如 range(1, 10, 2) 會產生 1,3,5,7,9（從 1 開始，每次加 2，直到小於 10）
for i in range(1, 10, 2):
    print(i)

import streamlit as st # 匯入 Streamlit 函式庫，用來建立簡易的網頁介面
number = st.number_input("請輸入一個數字", min_value=1, max_value=9)
for i in range()