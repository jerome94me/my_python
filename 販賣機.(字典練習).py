#建立菜單
menu ={
    "披薩": 300,
    "爆米花": 200,
    "薯條": 90,
    "洋芋片": 60,
    "軟麵包條": 120,
    "蘇打水" :60,
    "檸檬水" :90,

}
print("菜單")
print("--------------------------------------------------")
total = 0
cart =[]#空值
for item, price in menu.items():
    print(f"{item}:{price}")
#無窮循環
while True:
    food = input("請輸入一個菜單項目:(按下q結束)")
    if food == "q":
        break#中斷
    elif menu.get(food) is None:
        print("沒有這個商品,請重新輸入")
    else:
        cart.append(food)
        total += menu.get(food)
        print(food, end=" ")

print(f"總共{total}元")
