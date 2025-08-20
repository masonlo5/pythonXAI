## 🖥 我的程式學習重點整理

### 🔢 一、比較運算子（用來比大小）

| 運算子 | 意思       | 範例              |
| ------ | ---------- | ----------------- |
| `==`   | 是否相等   | `1 == 1` 是 True  |
| `!=`   | 是否不相等 | `1 != 1` 是 False |
| `<`    | 是否小於   | `1 < 2` 是 True   |
| `>`    | 是否大於   | `2 > 1` 是 True   |
| `<=`   | 小於或等於 | `1 <= 1` 是 True  |
| `>=`   | 大於或等於 | `1 >= 1` 是 True  |

👉 這些常用在 `if` 判斷裡面。

---

### 🧠 二、邏輯運算子（用來判斷真假）

| 運算子 | 用法說明                | 範例                      |
| ------ | ----------------------- | ------------------------- |
| `and`  | 兩邊都要 True 才是 True | `True and False` 是 False |
| `or`   | 有一邊是 True 就是 True | `True or False` 是 True   |
| `not`  | 反過來（True 變 False） | `not True` 是 False       |

---

### 🏁 三、`if` 條件判斷（讓電腦幫你做選擇）

```python
if 條件1:
    做這件事
elif 條件2:
    做別的事
else:
    都不是就做這個
```

📌 範例：密碼輸入

```python
if password == "1234":
    print("welcome back")
elif password == "5678":
    print("hello sam")
else:
    print("wrong password")
```

---

### 📊 四、Streamlit 小工具（讓網頁可以互動）

- `st.number_input()`：可以讓使用者輸入數字
- `st.write()`：可以把文字或變數顯示在畫面上
- `st.button()`：按鈕，點下去可以做事情
- `st.balloons()`：畫面放氣球
- `st.snow()`：畫面下雪 ❄️

📌 成績分級範例：

```python
if score >= 90:
    st.write("A")
elif score >= 80:
    st.write("B")
...
else:
    st.write("E")
```

---

### 🔁 五、for 迴圈（重複做一樣的事）

```python
for i in range(5):
    print(i)
```

📌 `range(1, 5)` 會印出 1 到 4，不包含 5。

📌 `range(1, 10, 2)` 表示從 1 開始，每次加 2，印出 1, 3, 5, 7, 9

---

### 🧮 六、list 串列（像一排裝東西的箱子）

```python
my_list = [1, 2, 3, "a", "b"]
```

- 可以用 `my_list[0]` 來拿第一個東西（索引從 0 開始）
- 用 `len(my_list)` 可以知道有幾個東西

📌 list 的操作：

| 操作     | 說明                   | 範例                           |
| -------- | ---------------------- | ------------------------------ |
| 讀取元素 | 用索引                 | `L[0]` 拿第一個                |
| 修改元素 | 用索引更改內容         | `L[0] = 100`                   |
| 刪除元素 | 用 `remove()`、`pop()` | `L.remove("a")` 刪掉第一個 "a" |

---

### 🔂 七、list 切片（只拿一部份）

```python
L = [1, 2, 3, "a", "b", "c"]
print(L[::2])  # 每隔 2 個拿一個 → [1, 3, "b"]
```

📌 語法是 `L[起始:結束:步長]`

---

### 📄 八、檔案處理（打開、讀取文字檔）

```python
f = open("資料夾/檔案.py", "r", encoding="utf-8")
內容 = f.read()
f.close()
```

✅ 用 `with open(...) as f:` 會自動關檔案，不用寫 `f.close()`

---

### ✏️ 九、字串判斷（看檔名）

```python
filename = "class1.md"
print(filename.endswith(".md"))  # 看是不是 .md 結尾
```

---

### 🔁 十、複製與參考（list 的陷阱！）

```python
a = [1, 2, 3]
b = a
b[0] = 100
print(a)  # 會印出 [100, 2, 3]，因為是同一個 list
```

✅ 如果要「複製」，要用 `b = a.copy()`，這樣就不會互相影響。
