import random

secret_num = random.randint(1, 100)
print("我想好了一个1-100的数字，快来猜！")

while True:
    guess = int(input("请输入你的猜测："))
    if guess > secret_num:
        print("太大了！再试试")
    elif guess < secret_num:
        print("太小了！再试试")
    else:
        print(f"恭喜你猜对了！数字就是{secret_num}")
        break
