print("歡迎來到cornhub")
print("在這裡你可以找到各種玉米")
註冊=input("是否註冊? Y註冊 N離開")

if 註冊 == "Y".upper():
    try:
        age = int(input("請輸入你的年齡:"))
    except ValueError:
        print("請輸入有效的數字！")
        exit()
elif 註冊 == "N".upper():
    exit() 
else:
    print("輸入大寫字母")
    exit()

if age <= 0:
    print("你還沒出生你就在看這個東西???")
    exit()
elif age >= 100:
    print("你都這麼老了還想進來這裡???")
    print("你走吧")
    exit()
elif age < 18:
    print("你需要滿18歲才能註冊") 
    exit()
else:
    print("你可以註冊")

重新輸入 = input("是否要重新輸入年齡？(Y/N)：")
if 重新輸入 == "Y".upper():
    try:
        age = int(input("請輸入你的年齡:"))
    except ValueError:
        print("請輸入有效的數字！")
        exit()
    
    if age <= 0:
        print("你還沒出生你就在看這個東西???")
        exit()
    elif age >= 100:
        print("你都這麼老了還想進來這裡???")
        print("你走吧")
        exit()
    elif age < 18:
        print("你需要滿18歲才能註冊") 
        exit()
    else:
        print("你可以註冊")
elif 重新輸入 == "N".upper():
    exit()
else:
    print("輸入無效")
    exit()