import time
import random

low = 1
high = 100
num = random.randint(low, high)  # 隨機產生 1~100 之間的數字
guesses = 0  # 記錄猜測次數

print(" 歡迎來到猜數字遊戲！")

# 無窮循環
while True:
    guess = int(input(f"請猜一個介於{low} 到 {high} 之間的數字！"))
    guesses += 1
    if guess < num:
        print("猜的數字太小")
    elif guess > num:
        print("猜的數字太小了")
    else:
        print(f"恭喜你猜對了! 這個數字就是{num}")
        print(f"你猜了{guesses}次")
        break