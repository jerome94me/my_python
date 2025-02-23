#提供要求
print("""""
    要求:  
    不能超過12個字元
    不能包含空格
    不能包含數字
    不能小於四個字元  
    不能有中文字
    """)
#提供名字
user_name = input("請輸入你的使用者名稱:")
#開始判斷
if len(user_name) > 12:
    print("你的使用者名稱已超過12個字元,不能註冊!")
    exit()
#找出有無空格
elif " " in user_name:
    print("你的使用者名稱不能有空格!")
    exit()
#判斷是否有非英文字的字元
elif not user_name.isalpha():
    print("你的使用者名稱不能包含數字或中文字!")
#判斷是否小於四個字元
elif len(user_name) < 4:
    print("你的使用者名稱不能小於四個字元")
#全部通過的話......
else:
    print("歡迎",user_name,"!")