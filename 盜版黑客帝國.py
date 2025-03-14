import random

def print_green(text):
    print("\033[92m{}\033[0m".format(text))

while True:
    # randint() 找出 1 到 10 的隨機整數
    random_number = random.randint(1, 10)
    print_green(random_number)
    