# dictionary
# 字典是一種可變的、無序的數據類型，使用鍵值對來存儲數據
# 例如：{"name": "Alice", "age": 30}
# 字典的基本操作包括：新增、刪除、修改和查詢
# 新增：my_dict["gender"] = "female"
# 刪除：del my_dict["age"]
# 修改：my_dict["name"] = "Bob"
# 查詢：print(my_dict["name"])
d = {"a": 1, "b": 2, "c": 3}

# CRUD_READ
print(d["a"])
print(d["b"])
print(d["c"])

# get the keys in the dict
print(d.keys())
for key in d.keys():
    print(key)

# get the values in the dict
print(d.values())
for value in d.values():
    print(value)

# get all the values in the dict
print(d.values())
for value in d.values():    
    print(value)

# get key-value in the dict
print(d.items())
for key, value in d.items():
    print(key, value)

# CRUD_CREATE
d["d"] = 4
print(d)

# CRUD_UPDATE
d["a"] = 10
print(d)

# CRUD_DELETE
d["a"] = 5
print(d)

# CRUD_DELETE
# delete dict use pop()
# if not key in dict, will raise KeyError
print(d.pop("a"))

print(d.pop("e", "not found"))

# dict length
print(len(d))

# check if key exists
print("a" in d) # True
print("e" in d) # False
