# and要所有都是true
temp=float(input("請輸入你現在的額頭溫度(請輸入小數點):"))
if temp > 36.4 and temp < 37.5:
    print("你現在沒發燒")
elif temp < 36.4:
    print("你的溫度太低")
else:
    print("你現在發燒了")
