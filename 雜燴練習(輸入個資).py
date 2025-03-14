def is_valid_phone_number(phone_number):
    return len(phone_number) == 10 and phone_number.isdigit()

def is_valid_username(username):
    if len(username) > 12:
        print("你的使用者名稱已超過12個字元")
        return False
    if " " in username:
        print("你的使用者名稱包含空格")
        return False
    if any(char in username for char in "!?@#$%^&*()"):
        print("你的使用者名稱包含不允許的符號")
        return False
    if len(username) < 4:
        print("你的使用者名稱小於四個字元")
        return False
    if any('\u4e00' <= char <= '\u9fff' for char in username):
        print("你的使用者名稱包含中文字")
        return False
    if any(char.isdigit() for char in username):
        print("你的使用者名稱包含數字")
        return False
    return True

def is_valid_password(password):
    if " " in password:
        print("你的密碼包含空格,請重新輸入")
        return False
    if len(password) <= 4:
        print("你的密碼小於四個字元,請重新輸入")
        return False
    if any('\u4e00' <= char <= '\u9fff' for char in password):
        print("你的密碼包含中文字,請重新輸入")
        return False
    if any(char.isdigit() for char in password):
        print("你的密碼包含數字,請重新輸入")
        return False
    return True

while True:
    get_phone_num = input("請輸入你的電話號碼 (10碼): ")
    if not is_valid_phone_number(get_phone_num):
        print("請輸入正確的電話號碼!")
        continue
    else:
        print("電話號碼驗證成功")
        break

while True:
    user_name = input("請輸入你的使用者名稱:")
    if not is_valid_username(user_name):
        continue
    else:
        print("你的使用者名稱是:", user_name)
        break

while True:
    password = input("請輸入你的密碼(按下e查看要求):")
    if password == "e":
        print("--------------------------------------------------------------------------------")
        print("不能包含空格")
        print("不能小於四個字元")
        print("不能有中文字")
        print("不能有數字")
        continue
    if not is_valid_password(password):
        continue
    else:
        print("你的密碼是:", password)
        print("註冊成功")
        exit()
        break
    
# Compare this snippet from python/Untitled-1.ipynb:
