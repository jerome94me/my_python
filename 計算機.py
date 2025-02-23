# 取得數字
num1=float (input("請輸入數字1:"))
num2=float (input("請輸入數字2:"))
加法=(num1 + num2)
減法=(num1 - num2)
乘法=(num1 * num2)
除法=(num1 / num2)

#取得運算符號
運算符號 = input("請選擇運算方法(要輸入大寫) A 加法,B 減法,C 乘法,D 除法").upper()
#執行條件
if 運算符號 == "A".upper():
    #轉換為整數
    print (int(加法))
elif 運算符號 == "B".upper():
    #轉換為整數
    print(int(減法))
elif 運算符號 == "C".upper():
    #轉換為整數
    print(int(乘法))
elif 運算符號 == "D".upper():
    #轉換為整數
    print(int(除法))
else:
    print("請輸入字母")
重複 = str(input("是否再算一次? Y(再一次) N(退出)")).upper()
if 重複 == "Y":
    運算符號 = input("請選擇運算方法 A 加法,B 減法,C 乘法,D 除法").upper()
    # 執行條件
    if 運算符號 == "A".upper():
        # 轉換為整數
        print(int(加法))
    elif 運算符號 == "B".upper():
        # 轉換為整數
        print(int(減法))
    elif 運算符號 == "C".upper():
        # 轉換為整數
        print(int(乘法))
    elif 運算符號 == "D".upper():
        # 轉換為整數
        print(int(除法))
    else:
        print("請輸入字母")
elif 重複 == "N".upper():
    print("感謝你使用我的爛東西")
    exit()
else:
   exit()