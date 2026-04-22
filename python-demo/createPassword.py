import random
import string


def generate_password(length=8):
    # 密码字符：字母+数字+符号
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = "".join(random.choice(chars) for _ in range(length))
    return password


# 生成10位密码
print("随机密码：", generate_password(10))
