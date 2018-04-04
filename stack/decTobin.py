#! venv/bin/python
#_*_ encoding:utf-8 _*_
"""
@Python -V: 3.X
@SoftWave: Pycharm
@OS: Ubuntu
@Author: SKYNE
@Contact: 520@skyne.cn
@Time: 2018.4.2
"""
from stack import stack

#  十进制整数转化为二进制字符串
def decTobin(decNumber):
    s = stack()

    while decNumber > 0:
        rem = decNumber % 2
        s.push(rem)
        decNumber = decNumber // 2

    binSting = ""
    while not s.isEmpty():
        binSting = binSting + str(s.pop())

    return binSting

if __name__ == '__main__':
    print(decTobin(99))     #1100011
