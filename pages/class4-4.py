# def
def hello_world():
    print("Hello, world!")


for i in range(10):
    hello()

def hello(name):
    print(f"Hello, {name}!")

hello("Alice")
hello("Bob")
hello("Charlie")
for i in range(10):
    hello(i)

def add(a, b):
    return a + b

print(add(1, 2))
print(add("Hello, ", "world!"))
sum = add(1, 2)
print(sum)

def add_subtract(a, b):
    return a - b, a + b

sum, sub = add_sub(5, 6)
print(f"sum = {sum}, sub = {sub}")

def add_sub(a, b):
   if a > b:
       return a + b
   else:
       return a - b
   
print(add_sub(5, 6))  # 5 - 6 = -1
print(add_sub(6, 5))  # 6 + 5 = 11

def hello(name, message="Hello"):