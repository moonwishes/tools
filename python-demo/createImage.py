from PIL import Image

# -------------- 这里改成你的图片路径 --------------
img_path = r"D:\Pictures\3.png"

# 1. 换更丰富的字符集（从密到疏，层次更多，更像原图）
char_set = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,\"^`'. "
# 2. 调大尺寸，保留更多细节
width = 120
height = 60

# 打开并处理图片
img = Image.open(img_path).convert("L")
img = img.resize((width, height))

result = ""
for y in range(height):
    for x in range(width):
        gray = img.getpixel((x, y))
        # 精准映射灰度到字符
        idx = int(gray * (len(char_set) - 1) / 255)
        result += char_set[idx]
    result += "\n"

# 保存
with open("高清字符画.txt", "w", encoding="utf-8") as f:
    f.write(result)

print("高清字符画生成完成！打开 高清字符画.txt 查看")
