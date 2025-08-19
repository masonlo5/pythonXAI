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

# 範例程式碼（以 Markdown code block 顯示，供學習參考）
st.markdown(
	"""
```python
a = 10
b = 3
print(f"a = {a}, b = {b}")
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")  # 小數除法
print(f"a // b = {a // b}")  # 整數除法
print(f"a % b = {a % b}")  # 取餘數
print(f"2 ** 3 = {2 ** 3}")
```
"""
)

# 同時顯示執行結果（使用教材中允許的語法）
a = 10
b = 3
st.write(f"執行結果範例： a = {a}，b = {b}")
st.write(f"a + b = {a + b}")
st.write(f"a - b = {a - b}")
st.write(f"a × b = {a * b}")
st.write(f"a ÷ b = {a / b}（小數）")
st.write(f"a // b = {a // b}（整數除法）")
st.write(f"a % b = {a % b}（取餘數）")
st.write(f"2 的 3 次方 = {2 ** 3}")

st.markdown("### 範例二：文字（字串）的玩法")
st.markdown("文字也可以像東西一樣相加或重複：")

# 顯示程式碼範例
st.markdown(
	"""
```python
name = "小明"
age = 9
print("說你好：" + " 你好")
print(name + " 很喜歡程式")
print(name * 2)
print(f"我是 {name}，我 {age} 歲。")
print(len(name))
```
"""
)

# 執行結果示範（教材中允許的語法）
name = "小明"
age = 9
st.write(name + " 很喜歡程式")
st.write(name * 2)
st.write(f"我是 {name}，我 {age} 歲。")
st.write(f"名字的長度：{len(name)} 個字")

st.markdown("### 範例三：看型態和換型態")
st.markdown("看一看這些東西的型態（它們是整數、浮點數還是字串），還有怎麼換型態：")

st.markdown(
	"""
```python
print(type(1))
print(type(1.0))
print(type('apple'))
print(int(1.0))
print(float(1))
print(str(1))
print(bool(1))
print(bool(0))
```
"""
)

# 顯示結果
st.write(f"type(1) -> {type(1)}")
st.write(f"type(1.0) -> {type(1.0)}")
st.write(f"type('apple') -> {type('apple')}")
st.write(f"int(1.0) -> {int(1.0)}")
st.write(f"float(1) -> {float(1)}")
st.write(f"str(1) -> {str(1)}")
st.write(f"bool(1) -> {bool(1)}（非零會是 True）")
st.write(f"bool(0) -> {bool(0)}（0 會是 False）")

st.markdown("---")
st.markdown("小提醒：以上範例只使用教材中出現過的語法與 API（如 f-string、len、type、int/float/str/bool、if/for/while、以及 st.title/st.write/st.text/st.markdown）。未在教材中出現的語法我沒有使用（若教材之後加入，新版筆記會自動納入）。")

st.markdown("### 補充一：List（串列）CRUD 範例與常用方法")
st.markdown("下面用簡單程式碼示範建立、讀取、更新與刪除（CRUD）操作，程式碼用 code block 顯示：")
st.markdown(
	"""
```python
# 建立
L = ["a", "b", "c", "d", "a"]

# 讀取
print(L[0])        # 第一個元素
print(L[-1])       # 最後一個元素
print(L[1:4])      # 切片

# 更新
L[0] = "z"       # 用索引指定新值
print(L)

# 刪除
L.remove("a")    # 刪除第一個匹配的元素
L.pop(0)           # 刪除指定索引
print(L)

# 複本
copy = L.copy()    # 淺拷貝
```
"""
)

# 範例輸出示範（使用靜態資料，避免在 Streamlit 執行互動輸入）
L = ["a", "b", "c", "d", "a"]
st.write("原始 L:", L)
st.write("L[0] ->", L[0], ", L[-1] ->", L[-1])
L[0] = "z"
st.write("更新後 L:", L)
L.remove("a")
st.write("刪除 'a' 後 L:", L)

st.markdown("### 補充二：迴圈（for / while）")
st.markdown("for 迴圈常用於走訪序列；while 可用於重複直到條件不成立。範例：")
st.markdown(
	"""
```python
# for 迴圈
for i in range(1, 4):
	print(i)

# 直接走訪 list
for x in ["a", "b", "c"]:
	print(x)

# while 範例
n = 3
while n > 0:
	print(n)
	n = n - 1
```
"""
)

st.write("for 範例輸出：", [1, 2, 3])
st.write("while 範例輸出：", [3, 2, 1])

st.markdown("### 補充三：檔案讀寫（open / with open）")
st.markdown("教材中示範過以 open() 與 with open() 讀取檔案，下面用 code block 示範：")
st.markdown(
	"""
```python
# 讀取（r）
f = open("pages/class1-1.py", "r", encoding="utf-8")
content = f.read()
f.close()

# 或使用 with 自動關閉
with open("pages/class1-1.py", "r", encoding="utf-8") as f:
	content = f.read()
	print(content[:80])  # 只顯示前 80 個字
```
"""
)

st.write("檔案讀取示範：會讀取教材檔案（僅示範，不會顯示全部內容）")

st.markdown("### 補充四：輸入 input() 與條件判斷 if/elif/else")
st.markdown("教材中也示範過 input() 與 if/elif/else，下面是示範程式碼（以 code block 顯示）：")
st.markdown(
	"""
```python
# 讀取使用者輸入（在命令列會等待輸入）
age = int(input("請輸入年齡："))

if age >= 18:
	print("你已成年")
elif age >= 13:
	print("你是青少年")
else:
	print("你是兒童")
```
"""
)

st.write("條件判斷示範（靜態範例）：", "當 age=18 時會顯示 '你已成年'。")

st.markdown("---")
st.markdown("小提醒：我把教材中已出現的指令與用法（例如 list CRUD、for/while、open/with、input、if/elif/else）補到筆記裡，程式碼範例皆以 Markdown code block 顯示；在 Streamlit 畫面中我以靜態變數示範輸出結果，避免直接在網頁呼叫會掛起的互動函式（例如 input()）。")

st.text("執行方式：在專案根目錄執行 \n1) pip install streamlit \n2) streamlit run pages/handbook.py")
