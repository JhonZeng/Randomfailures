import random
import keyboard

# 定义一个字母表，其中A-E的概率为其他字母的一半
# 正式使用前请用故障名代替字母修改字母表，并通过修改故障名后的数字来调整故障出现概率
alphabet = 'A' * 1 + 'B' * 1 + 'C' * 1 + 'D' * 1 + 'E' * 1 + \
           'F' * 2 + 'G' * 2 + 'H' * 2 + 'I' * 2 + 'J' * 2 + \
           'K' * 2 + 'L' * 2 + 'M' * 2 + 'N' * 2 + 'O' * 2 + \
           'P' * 2 + 'Q' * 2 + 'R' * 2 + 'S' * 2 + 'T' * 2 + \
           'U' * 2 + 'V' * 2 + 'W' * 2 + 'X' * 2 + 'Y' * 2 + 'Z' * 2


# 函数来随机选择一个故障
def random_letter():
    return random.choice(alphabet)


# 显示提示语
print("按下enter生成随机故障，按下esc退出程序")

# 主循环
try:
    while True:
        if keyboard.is_pressed('esc'):
            print("程序已退出")
            break
        elif keyboard.is_pressed('enter'):
            print(random_letter())
            while keyboard.is_pressed('enter'):
                pass  # Wait until the enter key is released
except KeyboardInterrupt:
    print("程序已停止")

# 该段代码需要确保已经安装了keyboard库。
# 可以使用pip install keyboard命令来安装它。
# 可能需要以管理员或root权限运行以便keyboard库能够正确监听键盘事件。
