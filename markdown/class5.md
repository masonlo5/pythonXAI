## 🧩 1. 函式可以有預設值

有時候，我們寫函式時，不一定每次都要給所有的參數。

```python
def hello(name, message="Hello"):
    print(f"{message}, {name}!")
```

📌 如果只輸入名字，它就會自己補上「Hello」！

---

## 🛠️ 2. 參數可以指定資料型態

這樣可以讓程式知道你要用的資料是什麼型態（像是數字或文字）。

```python
def add(a: int, b: int = 0) -> int:
    return a + b
```

📌 `a` 和 `b` 是整數（int），結果也會是整數。

---

## 🌍 3. 全域變數 和 區域變數

### ✅ 全域變數：寫在函式外面，大家都可以用

### ✅ 區域變數：寫在函式裡面，只能在裡面用

```python
length = 5

def calculate_square_area():
    area = length**2
    print("面積是", area)

calculate_square_area()
```

📌 `length` 是外面的變數（全域），`area` 是函式裡的變數（區域）。

---

## 🔁 4. 如果函式要改外面的變數，要加 `global`

```python
def calculate_square_area():
    global area
    area = length**2
```

📌 加了 `global` 才能改到外面的 `area`。

---

## 🧪 5. 函式可以回傳（return）結果

```python
def calculate_square_area() -> int:
    return length ** 2

area = calculate_square_area()
```

📌 用 `return` 可以把結果拿出來用。

---

## 🤖 6. 認識 `openai`：讓電腦可以跟我們聊天！

我們用 `openai` 來呼叫 AI 回答問題：

```python
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.chat.completions.create(
    model="gpt-5",
    messages=history,
)
```

📌 它會根據對話內容（history）來回應我們！

---

## 🧱 7. 用 `streamlit` 做簡單網頁

### ✨ 用 `st.chat_message()` 顯示對話

```python
st.chat_message("user").write("使用者說的話")
st.chat_message("assistant").write("AI 回答的話")
```

---

## 💬 8. 用 `streamlit` 做一個聊天頁面

我們可以儲存聊天紀錄（history），讓聊天不會被忘記！

```python
if "history" not in ss:
    ss.history = []

for message in ss.history:
    st.chat_message("user").write(message["content"])
```

還可以用 `st.chat_input()` 讓我們輸入問題。

---

## 🧹 9. 加上清除聊天按鈕

```python
if st.button("🗑️"):
    ss.history = [{"role": "system", "content": "請用中文回覆"}]
    st.rerun()
```

📌 一按下去，就能清除所有聊天紀錄。

---

## 🎉 我學會的技能

- 寫有預設值的函式
- 控制變數的範圍（全域/區域）
- 函式的回傳值
- 跟 AI 聊天（用 openai）
- 用 streamlit 做網頁和聊天介面
- 做出清除按鈕和聊天框
