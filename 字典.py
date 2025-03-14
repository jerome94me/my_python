#字典 dictionary
# 鍵 key
# 值 value
#設定字典
my_dictionary = {"a": 1, "b": 2, "c": 3}
#for in my_dictionary:
    #print(x)  
    # 這樣列出來會是鍵(key)

#正確方法
for key, value in my_dictionary.items():
    print("key:", key)
    print("value:", value)