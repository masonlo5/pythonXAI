# 比較運算子示範
# 比較運算子的回傳值為布林（True 或 False）
# 常見的比較運算子：
# ==  等於
# !=  不等於
# <   小於
# >   大於
# <=  小於等於
# >=  大於等於
# 比較運算通常用於條件判斷（if）、過濾資料或驗證輸入

print(1 == 1)  # True  -> 1 是否等於 1
print(1 != 1)  # False -> 1 是否不等於 1
print(1 < 1)   # False -> 1 是否小於 1
print(1 > 1)   # False -> 1 是否大於 1
print(1 <= 1)  # True  -> 1 是否小於或等於 1
print(1 >= 1)  # True  -> 1 是否大於或等於 1

# 進一步範例：字串比較（字典序比較）
print("a" < "b")  # True  -> 比較字母順序

# 型別注意事項：
# - 在 Python 3 中，不同型態的直接比較通常會拋出錯誤（例如 int 與 str 直接比較），
#   因此在比較前常需先確認型別或先行轉換。
# - 布林與數字可比較（True == 1、False == 0），但為了可讀性建議避免混用，改用明確比較。

# 邏輯運算子示範
# and：兩邊都為 True 時結果為 True，否則為 False
print(True and True)   # True
print(True and False)  # False
print(False and False) # False
print(False and True)  # False

# or：任一邊為 True 即為 True，兩邊皆 False 才為 False
print(True or True)    # True
print(True or False)   # True
print(False or False)  # False
print(False or True)   # True

# not：反轉布林值
print(not True)        # False
print(not False)       # True

# 運算子優先順序（由高到低，常見實務參考）
# 1. () 刮號
# 2. ** 次方
# 3. * / // % 乘除餘
# 4. + - 加 減
# 5. == != < > <= >= 比較運算子
# 6. not
# 7. and
# 8. or

# 範例：密碼門檢查（使用條件判斷）
password = input("請輸入密碼：")  # 讀取使用者輸入的密碼（字串）
if password == "1234":
    print("welcome back")  # 密碼為 1234
elif password == "5678":
    print("hello sam")     # 密碼為 5678
elif password == "0000":
    print("hello world")   # 密碼為 0000
else:
    print("wrong password")

# 註解說明：
# - 使用 if / elif / else 來檢查多個條件，第一個符合的分支會被執行。
# - elif 可以避免多個獨立 if 導致的重複檢查，使流程更清晰。
# - 輸入的內容預設為字串，若要比較數字需將輸入轉成 int 或 float。