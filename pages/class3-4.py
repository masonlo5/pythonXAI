import random

# 產生答案
# random.randint(a, b) 會回傳一個包含 a 與 b 的整數
answer = random.randint(1, 100)  # 程式會從 1 到 100 中隨機選一個數字作為答案

# 設定猜測範圍的上下界，用來提示玩家目前的可選範圍
max_num = 100
min_num = 1

print("歡迎來到猜數字遊戲！我已經選好了一個 1 到 100 之間的數字。")  # 開場提示
print("請開始猜吧！")  # 提示玩家開始輸入

# 主迴圈：反覆要求玩家輸入，直到猜中為止
while True:
    try:
        # input() 會回傳字串，需要用 int() 轉為整數
        # f-string 用法：f"...{變數}..."，可以把變數插入字串中
        guess = int(input(f"請輸入{min_num} 到 {max_num}的整數："))

        # 比較玩家輸入與答案的關係，並根據結果提示玩家
        if guess < answer:
            print("再大一點")  # 提示要猜更大的數
            # 若玩家猜的數字比目前的下界還大，更新下界
            if guess > min_num:
                min_num = guess
        elif guess > answer:
            print("再小一點")  # 提示要猜更小的數
            # 若玩家猜的數字比目前的上界還小，更新上界
            if guess < max_num:
                max_num = guess
        else:
            # 猜中時結束迴圈
            print("猜中了！恭喜你！")
            break
    except ValueError:
        # 捕捉非整數輸入，告知玩家輸入格式錯誤
        print("請輸入有效的整數喔！")
