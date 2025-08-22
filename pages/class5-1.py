# default value
def hello(name, message="Hello"):
    print(f"{message}, {name}!")

hello("Alice")
hello("Bob", "Hi")

# control the argument that pass in
# variable: type=default value
def add(a: int, b: int = 0) -> int:
    return a + b

print(add(1, 2))
print(add("Hello,", " world!"))

# def have global area and local area
length = 5

def calculate_square_area():
    area = length**2 # length is global area and area is local area
    # length  = length + 1
    print("area is", area)


calculate_square_area()
# print ("length is", area)

length = 5 # global area

def calculate_square_area():
    area = length**2  # length is global area and area is local area
    print("area is", area)

length = 10 # global area
calculate_square_area() # are is 100
# because need to wait for the function to finish executing before accessing local variables

length = 5 # global area
area = 100 # global area

def calculate_square_area():
    area = length**2 # length is global area and area is local area

calculate_square_area()
print("area is", area) # area is 100
# now area is local area

length = 5 # global area
area = 100 # global area

def calculate_square_area() -> int:
    area = length**2 # length is global area and area is local area
    return area

area = calculate_square_area()
print("area is", area) # area is 25

length = 5 # global area
area = 100 # global area

def calculate_square_area():
    global area # declare global area
    area = length**2 # length is global area and area is local area

calculate_square_area()
print("area is", area) # area is 25 


def hello(name: str): # declare parameter type
    print(f"Hello, {name}!")
