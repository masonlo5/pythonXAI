# 🧠 我的程式學習重點整理

## 📦 `import streamlit as st`

這一行是跟電腦說「我要用 Streamlit 這個工具」，才能做出網頁介面。

---

## 🏷️ 標題與按鈕排版（用 columns）

### ➤ `st.title("columns")`

這是網頁的標題，會出現在最上面。

### ➤ `col1, col2 = st.columns(2)`

這樣可以把畫面分成 2 欄，左邊是 `col1`，右邊是 `col2`。

### ➤ `col1.button("button1")`

這是在 `col1` 放一個按鈕，按了會有反應（不一定會做什麼事，要加程式才會有動作）。

### ➤ `st.columns([1, 2])`

這是設定欄位比例，左邊是 1 格，右邊是 2 格，右邊比較寬。

### ➤ `st.columns(3)`

這樣可以分成 3 欄，像三個區塊可以放不同東西。

### ➤ `with col1:`（或 col2, col3）

可以讓你在某一個欄位裡放多個東西，比如文字和按鈕放在一起。

---

## 🔄 迴圈做出很多欄位或按鈕

### ➤ `for i in range(n):`

這是一個迴圈，會重複做 n 次，讓你可以放很多個按鈕或東西，不用一個一個寫。

### ➤ `cols = st.columns(n)`

會產生 n 個欄位，把東西平均分開排好。

---

## 💾 session_state（記住變數）

### ➤ `st.session_state`

這是用來記住使用者做過的事，不會因為重新執行就忘記。

### ➤ `if "ans" not in st.session_state:`

這是判斷變數有沒有存在，如果沒有就先給它一個初始值。

### ➤ `st.session_state.ans += 1`

這是讓記住的變數加 1，每次按按鈕都會變大。

---

## 🛒 食物點餐機（加到購物車）

### ➤ `st.text_input("write dishes name")`

讓使用者輸入要點的菜名。

### ➤ `st.session_state.order = []`

建立一個空的清單，用來放點的菜。

### ➤ `ss_order.append(dishes)`

把菜加入購物車（就是清單）。

### ➤ `st.rerun()`

重新執行畫面，會更新顯示的內容。

---

## 🧮 數學運算與變數

```python
a += 1  # a = a + 1
a -= 1  # a = a - 1
a *= 2  # a = a * 2
a /= 2  # a = a / 2
a //= 2  # 無條件去除（整數）
a %= 2  # 取餘數
a **= 2  # 次方
```

### ➤ 運算順序（誰先算）：

1. 括號 `()`
2. 次方 `**`
3. 乘除 `* / // %`
4. 加減 `+ -`
5. 比大小 `== != < > <= >=`
6. `not`
7. `and`
8. `or`

---

## 🔁 while 跟 for 迴圈

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

- `while` 是「當...成立就一直做」
- `for` 是「做幾次就做幾次」

可以搭配一起用，也可以加 `break` 來提早跳出。

---

## 🎲 random 隨機數字

### ➤ `random.randrange(x)`

會從 0 到 x-1 中選一個數。

### ➤ `random.randint(a, b)`

會從 a 到 b（包含 a 和 b）選一個數。

---

## 🎯 猜數字遊戲

```python
answer = random.randint(1, 100)
```

- 程式會選一個 1\~100 的數字
- 玩家要猜，會有提示「再大一點」或「再小一點」
- 猜對了就結束！

---

## 🖋️ 輸入文字

```python
text = st.text_input("write something")
st.write(f"You wrote: {text}")
```

- 可以讓使用者輸入字
- 然後把輸入的內容印出來
