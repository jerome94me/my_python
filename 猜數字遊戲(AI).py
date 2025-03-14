import time
import random

low = 1
high = 100
num = random.randint(low, high)  # 隨機產生 1~100 之間的數字
guesses = 0  # 記錄猜測次數

print("🎯 歡迎來到猜數字遊戲！")
print(f"請猜一個介於 {low} 到 {high} 之間的數字！")

# 無窮循環
while True:
    try:
        guess = int(input("請輸入你的猜測: "))
        guesses += 1

        if guess < low or guess > high:
            print(f"⚠️ 請輸入 {low} 到 {high} 之間的數字！")
            continue  # 讓玩家重新輸入

        if guess < num:
            print("📉 太小了，再試一次！")
            low = guess + 1  # 調整最小範圍
        elif guess > num:
            print("📈 太大了，再試一次！")
            high = guess - 1  # 調整最大範圍
        else:
            print(f"🎉 恭喜你猜對了！答案是 {num}！")
            print(f"你總共猜了 {guesses} 次。")
            break  # 結束遊戲

    except ValueError:
        print("❌ 輸入錯誤！請輸入數字！")

time.sleep(1)  # 讓玩家看到結果後再結束
print("👋 感謝遊玩，再見！")
