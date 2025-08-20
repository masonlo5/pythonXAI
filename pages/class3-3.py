a = 1
a += 1 # a = a + 1
print(a)
a -= 1 # a = a - 1
print(a) # 1
a *= 2 # a = a * 2
print(a) # 2
a /= 2 # a = a / 2
print(a) # 1.0
a //= 2 # a = a // 2
print(a) # 0
a %= 2 # a = a % 2
print(a) # 0.0
a **= 2 # a = a ** 2
print(a) # 0.0

# 運算子優先順序（由高到低，常見實務參考）
# 1. () 刮號
# 2. ** 次方
# 3. * / // % 乘除餘
# 4. + - 加 減
# 5. == != < > <= >= 比較運算子
# 6. not
# 7. and
# 8. or

i = 0
while i < 5:
    print(i)
    i += 1 # i = i + 1

i = 0
while i < 5:
    print(i)

    for j in range(5):
        print(j)

    if i == 3:
        break # get out of the loop

    i = 0
    while i < 5:
        print(i)

        for j in range(5):
            print(j)

        if i == 3:
            break # get out of the loop

        i = 0
        while i < 5:
            print(i)

            for j in range(5):
                print(j)

            if i == 3:
                break # get out of the loop

            i += 1

import random


print(random.randrange(7))
print(random.randrange(1, 6))
print(random.randrange(1, 6, 2))  # 1, 3, 5

print(random.randint(1, 6))  # 1, 2, 3, 4, 5, 6