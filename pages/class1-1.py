# 這是註解，不會影響程式碼的執行
# command + ?  可以快速註解或取消註解選取的程式碼
# 這是註解，不會影響程式碼的執行

# 基本型態
print(1)  # int這是整數，-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
print (1.0)  # float這是浮點數
print(1.234)  # float這是浮點數
print("apple")  # str這是字串 "sadsad123125557" , '1'
print("1") # str這是字串 "1" , '1'
print(True)  # bool這是布林值，True或False
print(False)  # bool這是布林值，True或False

# 變數
a = 10 # 新增一個儲存格a，並將數值10儲存到a中，“＝”的作用是將右邊的值儲存到左邊的變數中
print(a)  # 在螢幕上顯示變數a的值
a = "apple" # 在變數a中儲存字串"apple"
print(a)  # 在螢幕上顯示變數a的值

# 運算子
print(1 + 1)  # 加法
print(1 - 1)  # 減法
print(1 * 1)  # 乘法
print(1 / 1)  # 除法
print(1 // 1)  # 整數除法
print(1 % 1)  # 取餘數
print(2 ** 3)  # 2的3次方

# 優先順序
# 1. () 刮號
# 2. ** 次方
# 3. * / // % 乘除餘
# 4. + - 加 減

# please use the words to finish other things

# 字串運算
print("apple" + "banana")  # 字串相加
print("apple" * 3)  # 字串重複

# 字串格式化
name = "apple"  # 字串變數
age = 18  # 整數變數
print(f"Hello, my name is {name} and I am {age} years old.")  # f-string格式化
# 可以使用f-string來格式化字串，將變數的值嵌入到字串中

# len() 函式可以取得字串的長度
print(len(name))  # 取得name的長度

# len() 函式可以取得字串的長度
print(type(1)) # <class 'int'>
print(type(1.0)) # <class 'float'>
print(type("apple")) # <class 'str'>
print(type(True)) # <class 'bool'>

# type() # 可以取得變數的型態
print(type(1)) # <class 'int'>
print(type(1.0)) # <class 'float'>
print(type("apple")) # <class 'str'>
print(type(True)) # <class 'bool'>

# 型別轉換
print(int(1.0))  # float轉整數
print(float(1))  # int轉浮點數
print(str(1))  # int轉字串
print(bool(1))  # int轉布林值
print(bool(0))  # int轉布林值，0為False，其他為True

print("輸入開始")
# input()是一個函式，可以讓使用者輸入資料
# input()會暫停程式的執行，等待使用者輸入資料
a = input("請輸入一個數字：")  # 等待使用者輸入
print("輸入結束")
print(int(a) + 10)
print(type(a))  # 輸入的資料是字串型態

a = int(input())
print(f"a * a * 3.14 = {a * a * 3.14}")
