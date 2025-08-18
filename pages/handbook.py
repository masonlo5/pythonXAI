import streamlit as st

# 小學生也能懂的程式筆記（將學過的內容整理在這裡）

st.title("程式小手冊 - 今天學到的東西")

# 簡短說明
st.markdown("""
下面用很簡單的句子介紹今天學的東西，並用小範例讓你看懂。
""")

st.markdown("### 今天的重點（簡單版）")
st.markdown("""
- 數字和文字：int、float、str、bool
- 變數：把東西放進箱子（變數）
- 運算：加、減、乘、除、整數除法、取餘數、次方
- 文字可以相加或重複
- f-string：把變數放進字串一起顯示
- len()、type()、和型別轉換（int/float/str/bool）
""")

st.text("　")
st.markdown("### 範例一：數字和基本運算")
st.markdown("請看下面的數字範例，想像 a、b 是兩個裝數字的箱子：")

# 範例變數和運算（只用最基本的東西）
a = 10
b = 3

st.write(f"a = {a}，b = {b}")
st.write(f"a + b = {a + b}")
st.write(f"a - b = {a - b}")
st.write(f"a × b = {a * b}")
st.write(f"a ÷ b = {a / b}（小數）")
st.write(f"a // b = {a // b}（整數除法）")
st.write(f"a % b = {a % b}（取餘數）")
st.write(f"2 的 3 次方 = {2 ** 3}")

st.markdown("### 範例二：文字（字串）的玩法")
st.markdown("文字也可以像東西一樣相加或重複：")
name = "小明"
age = 9
st.write("說你好：" + " 你好")
st.write(name + " 很喜歡程式")
st.write(name * 2)
st.write(f"我是 {name}，我 {age} 歲。")
st.write(f"名字的長度：{len(name)} 個字")

st.markdown("### 範例三：看型態和換型態")
st.markdown("看一看這些東西的型態（它們是整數、浮點數還是字串），還有怎麼換型態：")
st.write(f"type(1) -> {type(1)}")
st.write(f"type(1.0) -> {type(1.0)}")
st.write(f"type('apple') -> {type('apple')}")
st.write(f"int(1.0) -> {int(1.0)}")
st.write(f"float(1) -> {float(1)}")
st.write(f"str(1) -> {str(1)}")
st.write(f"bool(1) -> {bool(1)}（非零會是 True）")
st.write(f"bool(0) -> {bool(0)}（0 會是 False）")

st.markdown("---")
st.markdown("小提醒：以上都只用到今天學過的指令與語法，沒有用到還沒學的東西。你可以改變數字或文字，重新整理網頁看看結果。")
