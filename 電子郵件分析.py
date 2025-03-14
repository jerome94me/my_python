#設定email
email = "melovetyphoon@gmail.com"
#index簡介
#Index可以計算某個字元在計算中的哪一個位置
#先找出@
index = email.index("@")
#印出
print("你的@在第",index,"個字元")
#如果去掉index
print(email[:index])
#!不能雙引號
#如果要把gmail.com列出來呢?
print(email[(index+1):])
#要加一是要讓@不會跑出來