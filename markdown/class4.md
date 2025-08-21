### 一、📘 字典 Dictionary

字典就像一本小筆記本，用「名字（key）」來找到「內容（value）」。

例如：

```python
d = {"a": 1, "b": 2, "c": 3}
```

這是一本有三個項目的小筆記本：

- a 是 1
- b 是 2
- c 是 3

🔍 查詢：

```python
print(d["a"])  # 會顯示 1
```

🆕 新增資料：

```python
d["d"] = 4
```

✏️ 修改資料：

```python
d["a"] = 10
```

❌ 刪除資料：

```python
del d["a"]
```

也可以用：

```python
d.pop("a")  # 把 a 刪掉
```

🗝️ 其他功能：

- `d.keys()`：顯示所有名字（key）
- `d.values()`：顯示所有內容（value）
- `d.items()`：顯示所有名字和內容

🧐 判斷有沒有這個 key：

```python
"a" in d  # 回傳 True 或 False
```

---

### 二、🖼️ Streamlit 顯示圖片

我們用 `streamlit` 這個工具來做出簡單的網站，可以顯示圖片，也可以做出商店。

#### 🔍 顯示資料夾裡的圖片：

```python
image_files = os.listdir("image")
```

這行會找出所有圖片的檔名。

可以用 `st.image()` 顯示圖片：

```python
st.image("image/minecraft.png", width=300)
```

---

### 三、🛒 做一個小小商店

我們用程式來做出一個可以「買東西」的頁面！

我們幫每個商品記錄：

- 價格（price）
- 庫存（stock）
- 圖片（image）

資料會長這樣：

```python
{
  "mincraft": {"price": 10, "stock": 10, "image": "image/mincraft.png"}
}
```

✅ 功能有：

- 顯示所有商品
- 點按鈕可以買商品（庫存 -1）
- 管理員可以加庫存和改價格

---

### 四、🧮 函數 Function

函數就像是你自訂的一個小工具，讓你把常常要做的事情包起來！

#### 👋 簡單的函數：

```python
def hello_world():
    print("Hello, world!")
```

#### 👋 可以放名字：

```python
def hello(name):
    print(f"Hello, {name}!")
```

呼叫它：

```python
hello("Alice")
```

#### ➕ 加法函數：

```python
def add(a, b):
    return a + b
```

你可以加數字，也可以加文字：

```python
print(add(1, 2))             # 3
print(add("Hello, ", "world!"))  # Hello, world!
```

#### ➕➖ 加減一起算：

```python
def add_sub(a, b):
    return a - b, a + b
```

也可以做判斷：

```python
def add_sub(a, b):
   if a > b:
       return a + b
   else:
       return a - b
```
