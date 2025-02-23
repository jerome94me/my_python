#請使用者提供電話號碼
phone_num=input("請輸入你的電話號碼:")
#用replace來取代
phone_num = phone_num.replace("-"," ")
#輸出
print("你的電話號碼已經底線換成空格:",phone_num)