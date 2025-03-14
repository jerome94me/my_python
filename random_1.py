import random

# randint() 找出 1 到 10 的隨機整數
print(random.randint(1, 10))

# 生成 0.0 到 1.0 之間的隨機浮點數
print(random.random())

# 列表中隨機選擇元素
app = ["剪刀", "石頭", "布"]  # 先決定列表
rand_option = random.choice(app)  # 使用 random.choice() 而不是 choices()
print("電腦選擇的是:", rand_option)

# 將列表打亂
card = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
random.shuffle(card)
print(card)

# 提示: 這些玩意千萬不要加上 while True，避免死迴圈
