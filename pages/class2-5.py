# 這是註解，不會影響程式碼的執行
# command + ?  可以快速註解或取消註解選取的程式碼
# List（串列）是 Python 常用的序列型別，可以儲存零個或多個元素，元素之間以逗號分隔
# 使用中括號 [] 定義 list，list 可以包含任意型別，也可包含巢狀的 list
print([])  # 這是一個空的 list，尚未包含任何元素
print([1, 2, 3])  # 這個 list 有三個整數元素
print([1, 2, 3, ["a", "b", "c"]])  # 這個 list 有四個元素，最後一個元素本身是另一個 list（巢狀 list 的範例）
print([1, True, "a", 1.23])  # 這個 list 有四個元素，包含不同型別（int, bool, str, float）

# CRUD（建立 Create / 讀取 Read / 更新 Update / 刪除 Delete）是常見的資料操作概念
# 下面示範 Read（讀取）操作：使用索引（index）從 list 取出元素
# 注意：list 的索引從 0 開始，my_list[0] 代表第一個元素，負數索引可從尾端反向取值（例如 my_list[-1]）
my_list = [10, 20, 30, 40]  # 範例用的 list，方便示範讀取索引
print(my_list[0])  # 讀取第一個元素（index 0），結果為 10
print(my_list[1])  # 讀取第二個元素（index 1），結果為 20
print(my_list[2])  # 讀取第三個元素（index 2），結果為 30
print(my_list[3])  # 讀取第四個元素（index 3），結果為 40

L = [1, 2, 3, "a", "b", "c"]  # 範例 list，用於示範切片（slice）
# 切片語法：L[start:stop:step]
# start：起始索引（包含），stop：結束索引（不包含），step：步進（跳過元素的數量）
# 如果省略 start，預設從開頭開始；省略 stop，預設到結尾；省略 step，預設為 1
# 範例：L[::2] 表示從頭到尾，每隔 2 個元素取一次（step=2）
print(L[::2])  # 取得索引 0,2,4 -> [1, 3, 'b']
# L[1::2] 表示從 index 1 開始到尾端，每隔 2 個元素取一次
print(L[1::2])  # 取得索引 1,3,5 -> [2, 'a', 'c']
# L[1:4:2] 表示從 index 1（含）到 index 4（不含），每隔 2 個元素取一次
# 因此會取得 index 1 和 index 3 對應的元素，結果是 [2, 'a']
print(L[1:4:2])  # 取得索引 1 和 3 -> [2, 'a']
# 切片的行為類似於 range()，可用於選取區間或步進取樣

# 取得 list 長度（元素數量）：使用內建函式 len()
print(len(my_list))  # my_list 有 4 個元素，會輸出 4
print(len(L))  # L 有 6 個元素，會輸出 6

# List 走訪（iteration）元素的兩種常見寫法
L = [1, 2, 3, "a", "b", "c"]  # 範例 list，用於示範走訪（iteration）
# 方法一：使用索引（index）搭配 range()，可以控制步進與索引值
for i in range(0, len(L), 2):
    # 這裡每次取得的 i 是索引，使用 L[i] 取得對應元素
    print(L[i])  # 會依序印出索引 0,2,4 對應的元素

# 方法二：直接迭代 list 中的元素（更簡潔且常用）
for i in L:
    print(i)  # 會依序印出每個元素 1,2,3,'a','b','c'

# CRUD Update
L = [1, 2, 3, "a", "b", "c"]
# Update（更新）操作：透過索引直接指定新的值
L[0] = 100  # 將索引 0 的元素更新為 100（示範修改 list 的內容）
print(L)  # 印出更新後的 list，結果為 [100, 2, 3, 'a', 'b', 'c']

# Python 的變數賦值語意說明：對不可變型別（例如 int, str, tuple）看似「值傳遞」
# 對可變型別（例如 list, dict）則是賦值為參考（reference）到相同物件
# 範例：不可變型別（類似 call by value 的效果）
a = 1
b = a  # b 會得到 a 的值，兩者為獨立的物件（整數是不可變）
b = 2  # 修改 b 不會影響 a
print(a, b)  # 輸出 1 2

# 範例：可變型別（賦值為參考，修改會影響所有參考該物件的變數）
a = [1, 2, 3]  # a 是一個 list
b = a  # b 指向與 a 相同的 list（兩者為相同物件的兩個參考）
b[0] = 2  # 修改 b 的第一個元素，同時也改變 a
print(a, b)  # 會印出 [2, 2, 3] [2, 2, 3]

# 若想建立一個新複本而不影響原本的 list，可使用 copy() 建立淺拷貝
a = [1, 2, 3]  # a 是一個 list
b = a.copy()  # 使用 copy() 方法建立 a 的淺拷貝（新的 list 但元素為相同的參考）
b[0] = 2  # 修改 b 的第一個元素，不會影響 a
print(a, b)  # 會印出 [1, 2, 3] [2, 2, 3]

# 註：淺拷貝只會複製外層容器，若 list 中包含可變子物件（例如巢狀 list），
#     子物件仍然是共享參考；需要深拷貝可使用 copy.deepcopy()。

# CRUD Delete（刪除）
# List 刪除元素：可以使用 del、remove() 或 pop() 等方法
L = ["a", "b", "c", "d", "a"]
L.remove("a")  # remove("a") 會刪除第一個出現的 "a"
# remove() 會從串列開頭開始尋找並刪除第一個相符的元素
# 若要刪除所有出現的相同元素，請避免在 for 迴圈中直接修改串列（會導致行為不穩定）
# 安全的做法範例：使用 while 搭配 in，或建立新的串列（list comprehension）過濾
L = ["a", "b", "c", "d", "a"]
while "a" in L:
    L.remove("a")  # 逐一刪除直到沒有 "a" 為止

# 使用 pop() 可以指定索引刪除，或不帶參數刪除最後一個元素
L = ["a", "b", "c", "d", "a"]
L.pop(0)  # 刪除索引 0 的元素（第一個 "a"）
# L 會變成 ["b", "c", "d", "a"]
L.pop()  # 不指定索引則刪除最後一個元素（第二個 "a"）
print(L)  # L 會變成 ["b", "c", "d"]

# open() 開啟檔案的基本用法
# r-讀取模式
# w-寫入模式
# a-附加模式
# r+-讀寫模式
# w+-寫入模式（會覆蓋原有內容）
# a+-附加模式（會在檔案末尾新增內容）

f = open("pages/class1-1.py","r", encoding="utf-8")
content = f.read()  # 讀取檔案內容
print(content)  # 印出檔案內容
f.close()  # 關閉檔案
########################################
with open("pages/class1-1.py", "r", encoding="utf-8") as f:
    content = f.read()  # 使用 with 語句自動管理檔案開啟與關閉
    print(content)  # 印出檔案內容
# no need to call f.close(), it will be closed automatically

# 字串工具用來檢查與操作文字資料（範例：檔名判斷）
filename = "class1.md"
print(filename.endswith(".md"))  # True：判斷字串是否以 ".md" 結尾
filename2 = "nates.text"
print(filename2.endswith(".md"))  # False：判斷另一個檔名是否以 ".md" 結尾