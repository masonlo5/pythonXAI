- 加上 `#` 的文字是**註解**，只是寫給自己或別人看的，電腦不會執行。
- 可以用快捷鍵 `Command + ?` 把選到的程式變成註解，或取消註解。

---

## 🔢 基本資料的種類（資料型態）

### 數字：

```python
print(1)  # 整數（int）
print(1.0)  # 小數（float）
```

### 文字：

```python
print("apple")  # 文字（字串 str）
```

### 是或不是（True/False）：

```python
print(True)  # 布林值（bool）
print(False)
```

---

## 📦 變數是什麼？

- 變數就像是一個**盒子**，可以把東西裝進去。

```python
a = 10
print(a)  # 顯示a裡的東西

a = "apple"
print(a)  # a現在裝的是文字
```

---

## ➕➖ 會算數的程式（運算子）

```python
print(1 + 1)  # 加法
print(2 - 1)  # 減法
print(3 * 2)  # 乘法
print(4 / 2)  # 除法（會有小數）
print(5 // 2)  # 整數除法（只看整數）
print(5 % 2)  # 餘數
print(2 ** 3)  # 次方（2的3次方 = 8）
```

### 📐 算式的順序（很重要！）

1. () 括號最優先
2. \*\* 次方
3. 乘、除、整除、餘數
4. 加、減

---

## 🧵 字串的用法（文字的玩法）

### 字串相加、重複：

```python
print("apple" + "banana")  # 合起來變成一個字串
print("apple" * 3)  # 重複三次
```

### 字串加變數（f-string）：

```python
name = "apple"
age = 18
print(f"Hello, my name is {name} and I am {age} years old.")
```

---

## 📏 算長度、看型態（用函式）

### 算長度：

```python
print(len("apple"))  # 看有幾個字母
```

### 看型態：

```python
print(type(1))  # int
print(type(1.0))  # float
print(type("apple"))  # str
print(type(True))  # bool
```

---

## 🔁 變來變去（型別轉換）

```python
print(int(1.0))  # 小數變整數
print(float(1))  # 整數變小數
print(str(1))  # 數字變字串
print(bool(1))  # 變成True
print(bool(0))  # 變成False
```

---

## ⌨️ 讓使用者輸入（input）

```python
a = input("請輸入一個數字：")  # 輸入的東西會是字串
print(int(a) + 10)  # 變成整數後再加10
```

---

## 📏 練習：計算圓面積（半徑 × 半徑 × 3.14）

```python
a = int(input())
print(f"a * a * 3.14 = {a * a * 3.14}")
```

---

## 🖥️ Streamlit 的用法（做漂亮的畫面）

````python
import streamlit as st

st.title("這是標題")  # 顯示大標題
st.write("這是可以寫文字、數字等等的地方")
st.text("只能顯示文字的地方")

st.markdown("""
可以用Markdown語法寫格式：
* **粗體**
* *斜體*
* [連結](https://www.example.com)

```python
print("Hello, Streamlit!")
````

""")

```

---

## 🧱 標題等級（Markdown）
- `#` 是最大標題
- `##` 是第二大
- `###` 是第三大
- 最多可以到 `######`




```
