import random

# 定义一个字母表，其中A-E的概率为其他字母的一半
# 正式使用前请用故障名代替字母修改字母表，并通过修改故障名后的数字来调整故障出现概率
alphabet = 'A' * 1 + 'B' * 1 + 'C' * 1 + 'D' * 1 + 'E' * 1 + \
           'F' * 2 + 'G' * 2 + 'H' * 2 + 'I' * 2 + 'J' * 2 + \
           'K' * 2 + 'L' * 2 + 'M' * 2 + 'N' * 2 + 'O' * 2 + \
           'P' * 2 + 'Q' * 2 + 'R' * 2 + 'S' * 2 + 'T' * 2 + \
           'U' * 2 + 'V' * 2 + 'W' * 2 + 'X' * 2 + 'Y' * 2 + 'Z' * 2


# 函数来随机选择一个字母
def random_letter():
    return random.choice(alphabet)


# 主循环
try:
    while True:
        input("按下回车键获取一个随机字母...")
        print(random_letter())
except KeyboardInterrupt:
    print("程序已停止")

# 该段代码没有停止命令，只能通过关闭运行窗口或按下ctrl+c发送强制中断信号停止。
